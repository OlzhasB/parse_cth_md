import requests
import urllib3
import base64
import src.steel_tracks.hitachi.conf as conf
from bs4 import BeautifulSoup

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class LinksParser:
    def __init__(self):
        self.s = requests.session()
        self.details_links = self.get_details_links()

    def make_request(self, url, retries: int = 5):
        while retries > 0:
            try:
                r = self.s.get(url, timeout=10, verify=False)
                return r
            except requests.RequestException as e:
                print(f'Got network error while trying to make request to sms-parts.ru. Retrying {retries - 1}. {e}')
                retries -= 1

    def get_models_links(self):
        models_links = []
        r = self.make_request(conf.HITACH_LINK)
        soup = BeautifulSoup(r.text, 'lxml')
        div_s = soup.find_all('div', class_='buton32')
        for div in div_s:
            print(len(models_links))
            href = div.find('a').get('href')
            r = self.make_request(conf.CTH_URL + href)
            soup = BeautifulSoup(r.text, 'lxml')
            div_s2 = soup.find_all('div', class_='buton32')
            if div_s2:
                for div2 in div_s2:
                    href2 = div2.find('a').get('href')
                    models_links.append(href2)
                continue
            models_links.append(href)
        return models_links

    def links_init(self):
        links_dict = {}
        links_dict['Track group'] = []
        links_dict['Track chain'] = []
        links_dict['Track shoe'] = []
        links_dict['Track bolt'] = []
        links_dict['Track nut'] = []
        links_dict['Roller 1 Fl'] = []
        links_dict['Carrier Roller'] = []
        links_dict['Segment group'] = []
        links_dict['Idler 1'] = []
        return links_dict

    def get_details_links(self):
        links_dict = self.links_init()
        models_links = self.get_models_links()
        i = 0
        for models_link in models_links:
            r = self.make_request(conf.CTH_URL+models_link)
            soup = BeautifulSoup(r.text, 'lxml')
            rows = soup.find_all('tr')
            for row in rows:
                div_s = row.find_all('div')
                key = div_s[0].text.strip()
                value = div_s[1].find('a').get('href')
                i += 1
                links_dict[key].append(value)
        return links_dict

    def get_equipment_list(self, equipment):
        marks = equipment.find_all('div')
        models = equipment.find_all('table')
        str = ''
        i = 0
        for mark in marks:
            if i > 0:
                str += '; '
            str += mark.text.strip()
            model = models[i]
            rows = model.find_all('tr')
            j = 0
            for row in rows:
                td_s = row.find_all('td')
                for td in td_s:
                    if td.find('a'):
                        if j > 0:
                            str += ','
                        str += ' ' + td.text.strip()
                    j += 1
            i += 1
        return str

    def get_cross_reference_list(self, cross_reference):
        str = ''
        table = cross_reference
        rows = table.find_all('tr')
        i = 0
        for row in rows:
            td_s = row.find_all('td')
            if i > 0:
                str += ', '
            str += td_s[0].text.strip() + ' ' + td_s[1].text.strip()
            i += 1
        return str

    def get_details_list(self, details):
        str = ''
        table = details
        rows = table.find_all('tr')
        j = 0
        for row in rows:
            if j > 0:
                str += '; '
            td_s = row.find_all('td')
            i = 0
            for td in td_s:
                div_s = td.find_all('div')
                if div_s:
                    if i > 0:
                        str += '; '
                    str += div_s[0].text.strip() + ' ' + div_s[1].text.strip()
                i += 1
            j += 1
        return str

    def get_template_detail_info(self, links):
        info_list = []
        for link in links:
            info_dict = {}
            r = self.make_request(conf.CTH_URL + link)
            soup = BeautifulSoup(r.text, 'lxml')
            div = soup.find('div', id='sideright')

            div_s = div.find_all('div', class_=None)
            values = div_s[0].find_all('a')
            try:
                print(len(info_list))
                info_dict['Brand'] = values[0].text.strip()
                info_dict['Type'] = values[1].text.strip()
                info_dict['Model'] = values[2].text.strip()

                info_dict['Article'] = div_s[3].text.strip()
                info_dict['Weight'] = div_s[5].find_all('span')[1].text.strip().split(' ')[0]

                info_dict['Details'] = None
                details = soup.find('table', class_='tabella')
                if details:
                    info_dict['Details'] = self.get_details_list(details)

                equipment = soup.find('div', style='margin:10px;').previous_element
                info_dict['Equipment'] = self.get_equipment_list(equipment)

                info_dict['Cross Reference'] = None
                cross_reference = soup.find('table', class_='tabelref')
                if cross_reference:
                    info_dict['Cross Reference'] = self.get_cross_reference_list(cross_reference)

                info_dict['Image'] = None
                div_image = soup.find('div', class_='plansa')
                if div_image:
                    info_dict['Image'] = div_image.find('img').get('src').split('/')[1].split('.')[0]

                info_list.append(info_dict)
            except:
                pass
        return info_list


    def get_images_content(self):
        links = conf.images_links
        image_list = []
        for link in links:
            image_info = {}
            retries = 5
            while retries > 0:
                try:
                    image_info['code'] = base64.b64encode(requests.get(conf.CTH_URL + link, verify=False).content)
                    break
                except requests.RequestException as e:
                    print(
                        f'Got network error while trying to make request to sms-parts.ru. Retrying {retries - 1}. {e}')
                    retries -= 1
            image_info['name'] = link.split('/')[1].split('.')[0]
            image_list.append(image_info)
        return image_list

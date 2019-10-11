from src.steel_tracks.hitachi.psql import connect_to_psql, PSQL_USER, PSQL_PORT, PSQL_HOST, PSQL_DB, PSQL_PASSWORD
from src.steel_tracks.hitachi.psql import Base, TrackGroup, TrackChain, TrackShoe, TrackBolt, TrackNut
from src.steel_tracks.hitachi.psql import RollerFl, CarrierRoller, SegmentGroup, Idler1, Image
from src.steel_tracks.hitachi.parse import LinksParser

session, engine = connect_to_psql(PSQL_USER, PSQL_PASSWORD, PSQL_DB, PSQL_HOST, PSQL_PORT)
Base.metadata.create_all(engine)


def track_group_to_db(info):
    for t in info:
        tg = TrackGroup()
        tg.brand = t['Brand']
        tg.type = t['Type']
        tg.model = t['Model']
        tg.article = t['Article']
        tg.weight = t['Weight']
        tg.equipment = t['Equipment']
        tg.cross_reference = t['Cross Reference']
        session.add(tg)
    session.commit()


def track_chain_to_db(info):
    for t in info:
        tc = TrackChain()
        tc.brand = t['Brand']
        tc.type = t['Type']
        tc.model = t['Model']
        tc.article = t['Article']
        tc.weight = t['Weight']
        tc.details = t['Details']
        tc.equipment = t['Equipment']
        tc.cross_reference = t['Cross Reference']
        tc.image = make_query_images(t['Image'])
        session.add(tc)
    session.commit()

def track_shoe_to_db(info):
    for t in info:
        ts = TrackShoe()
        ts.brand = t['Brand']
        ts.type = t['Type']
        ts.model = t['Model']
        ts.article = t['Article']
        ts.weight = t['Weight']
        ts.details = t['Details']
        ts.equipment = t['Equipment']
        ts.cross_reference = t['Cross Reference']
        ts.image = make_query_images(t['Image'])
        session.add(ts)
    session.commit()


def track_bolt_to_db(info):
    for t in info:
        tb = TrackBolt()
        tb.brand = t['Brand']
        tb.type = t['Type']
        tb.model = t['Model']
        tb.article = t['Article']
        tb.weight = t['Weight']
        tb.details = t['Details']
        tb.equipment = t['Equipment']
        tb.cross_reference = t['Cross Reference']
        tb.image = make_query_images(t['Image'])
        session.add(tb)
    session.commit()


def track_nut_to_db(info):
    for t in info:
        tn = TrackNut()
        tn.brand = t['Brand']
        tn.type = t['Type']
        tn.model = t['Model']
        tn.article = t['Article']
        tn.weight = t['Weight']
        tn.details = t['Details']
        tn.equipment = t['Equipment']
        tn.cross_reference = t['Cross Reference']
        tn.image = make_query_images(t['Image'])
        session.add(tn)
    session.commit()


def roller_fl_to_db(info):
    for t in info:
        rf = RollerFl()
        rf.brand = t['Brand']
        rf.type = t['Type']
        rf.model = t['Model']
        rf.article = t['Article']
        rf.weight = t['Weight']
        rf.details = t['Details']
        rf.equipment = t['Equipment']
        rf.cross_reference = t['Cross Reference']
        rf.image = make_query_images(t['Image'])
        session.add(rf)
    session.commit()


def carrier_roller_to_db(info):
    for t in info:
        rf = CarrierRoller()
        rf.brand = t['Brand']
        rf.type = t['Type']
        rf.model = t['Model']
        rf.article = t['Article']
        rf.weight = t['Weight']
        rf.details = t['Details']
        rf.equipment = t['Equipment']
        rf.cross_reference = t['Cross Reference']
        rf.image = make_query_images(t['Image'])
        session.add(rf)
    session.commit()


def idler1_to_db(info):
    for t in info:
        idl = Idler1()
        idl.brand = t['Brand']
        idl.type = t['Type']
        idl.model = t['Model']
        idl.article = t['Article']
        idl.weight = t['Weight']
        idl.details = t['Details']
        idl.equipment = t['Equipment']
        idl.cross_reference = t['Cross Reference']
        idl.image = make_query_images(t['Image'])
        session.add(idl)
    session.commit()

def segment_group_to_db(info):
    for t in info:
        sg = SegmentGroup()
        sg.brand = t['Brand']
        sg.type = t['Type']
        sg.model = t['Model']
        sg.article = t['Article']
        sg.weight = t['Weight']
        sg.details = t['Details']
        sg.equipment = t['Equipment']
        sg.cross_reference = t['Cross Reference']
        sg.image = make_query_images(t['Image'])
        session.add(sg)
    session.commit()


def make_query_images(name) -> int:
    images = session.query(Image)
    images = list(images)
    for image in images:
        if image.name == name:
            return image.id


def images_to_db(info):
    for i in info:
        img = Image()
        img.name = i['name']
        img.code = i['code']
        session.add(img)
    session.commit()


if __name__ == '__main__':
    parser = LinksParser()
    track_group_to_db(parser.get_template_detail_info(parser.details_links['Track group']))

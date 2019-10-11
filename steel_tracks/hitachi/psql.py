import os
from sqlalchemy import Column, Integer, String, Text, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


Base = declarative_base()
PSQL_USER = os.environ.get('POSTGRES_USER', 'postgres')
PSQL_PASSWORD = os.environ.get('POSTGRES_PASSWORD', 'postgres')
PSQL_HOST = os.environ.get('POSTGRES_HOST', 'localhost')
PSQL_DB = os.environ.get('POSTGRES_DB', 'hitachi')
PSQL_PORT = os.environ.get('POSTGRES_PORT', '5432')


def connect_to_psql(user: str, password: str, db_name: str, host: str, port):
    url = f'postgresql://{user}:{password}@{host}:{port}/{db_name}'
    engine = create_engine(url, client_encoding='utf-8', connect_args={"options": "-c timezone=Asia/Almaty"})
    db_session = sessionmaker(bind=engine)
    session = db_session()
    return session, engine


class TrackGroup(Base):
    __tablename__ = 'track_groups'
    id = Column(Integer, primary_key=True)
    brand = Column(String(255))
    type = Column(String(255))
    model = Column(String(255))
    article = Column(String(255))
    weight = Column(Float)
    equipment = Column(Text)
    cross_reference = Column(Text)


class TrackChain(Base):
    __tablename__ = 'track_chains'
    id = Column(Integer, primary_key=True)
    brand = Column(String(255))
    type = Column(String(255))
    model = Column(String(255))
    article = Column(String(255))
    weight = Column(Float)
    details = Column(Text)
    equipment = Column(Text)
    cross_reference = Column(Text)
    image = Column(Integer, ForeignKey('images.id'))

class TrackShoe(Base):
    __tablename__ = 'track_shoes'
    id = Column(Integer, primary_key=True)
    brand = Column(String(255))
    type = Column(String(255))
    model = Column(String(255))
    article = Column(String(255))
    weight = Column(Float)
    details = Column(Text)
    equipment = Column(Text)
    cross_reference = Column(Text)
    image = Column(Integer, ForeignKey('images.id'))

class TrackBolt(Base):
    __tablename__ = 'track_bolts'
    id = Column(Integer, primary_key=True)
    brand = Column(String(255))
    type = Column(String(255))
    model = Column(String(255))
    article = Column(String(255))
    weight = Column(Float)
    details = Column(Text)
    equipment = Column(Text)
    cross_reference = Column(Text)
    image = Column(Integer, ForeignKey('images.id'))


class TrackNut(Base):
    __tablename__ = 'track_nuts'
    id = Column(Integer, primary_key=True)
    brand = Column(String(255))
    type = Column(String(255))
    model = Column(String(255))
    article = Column(String(255))
    weight = Column(Float)
    details = Column(Text)
    equipment = Column(Text)
    cross_reference = Column(Text)
    image = Column(Integer, ForeignKey('images.id'))


class RollerFl(Base):
    __tablename__ = 'rollers_fl'
    id = Column(Integer, primary_key=True)
    brand = Column(String(255))
    type = Column(String(255))
    model = Column(String(255))
    article = Column(String(255))
    weight = Column(Float)
    details = Column(Text)
    equipment = Column(Text)
    cross_reference = Column(Text)
    image = Column(Integer, ForeignKey('images.id'))


class CarrierRoller(Base):
    __tablename__ = 'carrier_rollers'
    id = Column(Integer, primary_key=True)
    brand = Column(String(255))
    type = Column(String(255))
    model = Column(String(255))
    article = Column(String(255))
    weight = Column(Float)
    details = Column(Text)
    equipment = Column(Text)
    cross_reference = Column(Text)
    image = Column(Integer, ForeignKey('images.id'))


class SegmentGroup(Base):
    __tablename__ = 'segment_groups'
    id = Column(Integer, primary_key=True)
    brand = Column(String(255))
    type = Column(String(255))
    model = Column(String(255))
    article = Column(String(255))
    weight = Column(Float)
    details = Column(Text)
    equipment = Column(Text)
    cross_reference = Column(Text)
    image = Column(Integer, ForeignKey('images.id'))

class Idler1(Base):
    __tablename__ = 'idlers1'
    id = Column(Integer, primary_key=True)
    brand = Column(String(255))
    type = Column(String(255))
    model = Column(String(255))
    article = Column(String(255))
    weight = Column(Float)
    details = Column(Text)
    equipment = Column(Text)
    cross_reference = Column(Text)
    image = Column(Integer, ForeignKey('images.id'))


class Image(Base):
    __tablename__ = 'images'
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    code = Column(Text)
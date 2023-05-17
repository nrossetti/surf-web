from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, TIMESTAMP, DECIMAL, Float

Base = declarative_base()

class PlayerRank(Base):
    __tablename__ = 'ck_playerrank'

    steamid = Column(String(32), primary_key=True)
    steamid64 = Column(String(64))
    name = Column(String(64))
    country = Column(String(32))
    countryCode = Column(String(3))
    continentCode = Column(String(3))
    points = Column(Integer, default=0)
    wrpoints = Column(Integer, nullable=False, default=0)
    wrbpoints = Column(Integer, nullable=False, default=0)
    wrcppoints = Column(Integer, nullable=False, default=0)
    top10points = Column(Integer, nullable=False, default=0)
    groupspoints = Column(Integer, nullable=False, default=0)
    mappoints = Column(Integer, nullable=False, default=0)
    bonuspoints = Column(Integer, nullable=False, default=0)
    finishedmaps = Column(Integer, default=0)
    finishedmapspro = Column(Integer, default=0)
    finishedbonuses = Column(Integer, nullable=False, default=0)
    finishedstages = Column(Integer, nullable=False, default=0)
    wrs = Column(Integer, nullable=False, default=0)
    wrbs = Column(Integer, nullable=False, default=0)
    wrcps = Column(Integer, nullable=False, default=0)
    top10s = Column(Integer, nullable=False, default=0)
    groups = Column(Integer, nullable=False, default=0)
    lastseen = Column(Integer)
    joined = Column(Integer, nullable=False)
    timealive = Column(Integer, nullable=False, default=0)
    timespec = Column(Integer, nullable=False, default=0)
    connections = Column(Integer, nullable=False, default=1)
    readchangelog = Column(Integer, nullable=False, default=0)
    style = Column(Integer, nullable=False, default=0)

class LatestRecords(Base):
    __tablename__ = 'ck_latestrecords '

    steamid = Column(String(32), primary_key=True)
    steamid64 = Column(String(64))
    name = Column(String(64))
    country = Column(String(32))
    countryCode = Column(String(3))
    continentCode = Column(String(3))
    points = Column(Integer, default=0)
    wrpoints = Column(Integer, nullable=False, default=0)
    wrbpoints = Column(Integer, nullable=False, default=0)
    wrcppoints = Column(Integer, nullable=False, default=0)
    top10points = Column(Integer, nullable=False, default=0)
    groupspoints = Column(Integer, nullable=False, default=0)
    mappoints = Column(Integer, nullable=False, default=0)
    bonuspoints = Column(Integer, nullable=False, default=0)
    finishedmaps = Column(Integer, default=0)
    finishedmapspro = Column(Integer, default=0)
    finishedbonuses = Column(Integer, nullable=False, default=0)
    finishedstages = Column(Integer, nullable=False, default=0)
    wrs = Column(Integer, nullable=False, default=0)
    wrbs = Column(Integer, nullable=False, default=0)
    wrcps = Column(Integer, nullable=False, default=0)
    top10s = Column(Integer, nullable=False, default=0)
    groups = Column(Integer, nullable=False, default=0)
    lastseen = Column(Integer)
    joined = Column(Integer, nullable=False)
    timealive = Column(Integer, nullable=False, default=0)
    timespec = Column(Integer, nullable=False, default=0)
    connections = Column(Integer, nullable=False, default=1)
    readchangelog = Column(Integer, nullable=False, default=0)
    style = Column(Integer, nullable=False, default=0)

class LatestRecord(Base):
    __tablename__ = 'ck_latestrecords'

    steamid = Column(String(32), primary_key=True)
    name = Column(String(64))
    runtime = Column(DECIMAL(12, 6), nullable=False, default=-1.000000)
    map = Column(String(32), primary_key=True)
    date = Column(TIMESTAMP, nullable=False, server_default='CURRENT_TIMESTAMP')

    
class MapTier(Base):
    __tablename__ = 'ck_maptier'

    mapname = Column(String(54), primary_key=True)
    tier = Column(Integer)
    maxvelocity = Column(Float)
    announcerecord = Column(Integer, nullable=False, default=0)
    gravityfix = Column(Integer, nullable=False, default=1)
    ranked = Column(Integer, nullable=False, default=1)
    stages = Column(Integer)
    bonuses = Column(Integer)
    mapper = Column(String(255))


class Wrcps(Base):
    __tablename__ = 'ck_wrcps'

    mapname = Column(String(54), primary_key=True)
    tier = Column(Integer)
    maxvelocity = Column(Float)
    announcerecord = Column(Integer, nullable=False, default=0)
    gravityfix = Column(Integer, nullable=False, default=1)
    ranked = Column(Integer, nullable=False, default=1)
    stages = Column(Integer)
    bonuses = Column(Integer)
    mapper = Column(String(255))

class PrInfo(Base):
    __tablename__ = 'ck_prinfo'

    steamid = Column(String(32), primary_key=True)
    name = Column(String(64))
    mapname = Column(String(32), nullable=False)
    runtime = Column(DECIMAL(12, 6), nullable=False, default=-1.000000)
    zonegroup = Column(Integer, nullable=False, default=0)
    PRtimeinzone = Column(DECIMAL(12, 6), nullable=False, default=0.000000)
    PRcomplete = Column(Float, nullable=False, default=0)
    PRattempts = Column(Float, nullable=False, default=0)
    PRstcomplete = Column(Float, nullable=False, default=0)
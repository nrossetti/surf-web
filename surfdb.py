from sqlalchemy import create_engine, select, func, and_, not_, exists
from surftimer import *
#import configparser
import os

#CONFIG_PATH = 'config.ini'  
#CONFIG = configparser.RawConfigParser()
#CONFIG.read(CONFIG_PATH)

API_KEY = os.environ.get('HOSTNAME')
ADDRESS = os.environ.get('USERNAME')
PORT = os.environ.get('PASSWORD')
IMG_DIR = os.environ.get('DB')

#DB_HOST = str(CONFIG.get('surfdb', 'HOSTNAME'))
#DB_USER = str(CONFIG.get('surfdb', 'USERNAME'))
#DB_PASS = str(CONFIG.get('surfdb', 'PASSWORD'))
#DB_NAME = str(CONFIG.get('surfdb', 'DB'))

# Create a SQLAlchemy engine
engine = create_engine(f'mysql+mysqlconnector://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}')

def get_players():
    # Create a SELECT statement to query all rows from the ck_playerrank table
    stmt = select(PlayerRank.__table__).\
    group_by(PlayerRank.__table__.c.steamid64).\
    order_by(PlayerRank.__table__.c.lastseen.desc())

    # Execute the SELECT statement and fetch all rows
    with engine.connect() as conn:
        rows = conn.execute(stmt).fetchall()

    # Get the column names from the PlayerRank table
    column_names = PlayerRank.__table__.columns.keys()

    # Convert the rows to a list of dictionaries
    data = [dict(zip(column_names, row)) for row in rows]
    
    return data

def get_player(steamid64):
    # Create a SELECT statement to query the row for the given steamid64 from the ck_playerrank table
    stmt = select(PlayerRank.__table__).\
        where(PlayerRank.steamid64 == steamid64)

    # Execute the SELECT statement and fetch the row
    with engine.connect() as conn:
        row = conn.execute(stmt).fetchone()

    # If no row is found, return None
    if row is None:
        return None

    # Get the column names from the PlayerRank table
    column_names = PlayerRank.__table__.columns.keys()

    # Convert the row to a dictionary
    data = dict(zip(column_names, row))

    return data


def get_top():
    # Create a SELECT statement to query all rows from the ck_playerrank table
    stmt = select(PlayerRank.__table__).\
    order_by(PlayerRank.points.desc()).\
    limit(40)

    # Execute the SELECT statement and fetch all rows
    with engine.connect() as conn:
        rows = conn.execute(stmt).fetchall()

    # Get the column names from the PlayerRank table
    column_names = PlayerRank.__table__.columns.keys()

    # Convert the rows to a list of dictionaries
    data = [dict(zip(column_names, row)) for row in rows]
    
    return data

def get_latest():
    # Create a SELECT statement to query all rows from the ck_playerrank table
    stmt = select(LatestRecord.__table__).\
    order_by(LatestRecord.date.desc()).\
    limit(40)
    

    # Execute the SELECT statement and fetch all rows
    with engine.connect() as conn:
        rows = conn.execute(stmt).fetchall()

    # Get the column names from the PlayerRank table
    column_names = LatestRecord.__table__.columns.keys()

    # Convert the rows to a list of dictionaries
    data = [dict(zip(column_names, row)) for row in rows]
    
    return data


def get_maps():
    # Create a SELECT statement to query all rows from the ck_playerrank table
    stmt = select(MapTier.__table__).\
    order_by(MapTier.tier.asc(), MapTier.mapname)

    # Execute the SELECT statement and fetch all rows
    with engine.connect() as conn:
        rows = conn.execute(stmt).fetchall()

    # Get the column names from the PlayerRank table
    column_names = MapTier.__table__.columns.keys()

    # Convert the rows to a list of dictionaries
    data = [dict(zip(column_names, row)) for row in rows]
    
    return data

def get_maptier(mapname):
    # Create a SELECT statement to query all rows from the ck_playerrank table
    stmt = select(MapTier.__table__).\
    order_by(MapTier.tier.asc(), MapTier.mapname)

    # Execute the SELECT statement and fetch all rows
    with engine.connect() as conn:
        rows = conn.execute(stmt).fetchall()

    # Get the column names from the PlayerRank table
    column_names = MapTier.__table__.columns.keys()

    # Convert the rows to a list of dictionaries
    data = [dict(zip(column_names, row)) for row in rows]
    
    return data

def get_maprec(mapname):
    # Create a SELECT statement to query all rows from the ck_playerrank table
    stmt = select(PrInfo.__table__).\
        where(and_( PrInfo.mapname == mapname, PrInfo.zonegroup == 0, PrInfo.runtime > 0)).\
    order_by(PrInfo.runtime.asc())

    # Execute the SELECT statement and fetch all rows
    with engine.connect() as conn:
        rows = conn.execute(stmt).fetchall()

    # Get the column names from the PlayerRank table
    column_names = PrInfo.__table__.columns.keys()

    # Convert the rows to a list of dictionaries
    data = [dict(zip(column_names, row)) for row in rows]  

    return data

def get_playerrecs(steamid):
    # Create a SELECT statement to query all rows from the ck_playerrank table
    stmt = select(PrInfo.__table__).\
        where(and_( PrInfo.steamid == steamid, PrInfo.zonegroup == 0, PrInfo.runtime > 0)).\
    order_by(PrInfo.mapname.asc())

    # Execute the SELECT statement and fetch all rows
    with engine.connect() as conn:
        rows = conn.execute(stmt).fetchall()

    # Get the column names from the PlayerRank table
    column_names = PrInfo.__table__.columns.keys()

    # Convert the rows to a list of dictionaries
    data = [dict(zip(column_names, row)) for row in rows]  

    return data

def get_steamid(steamid64):
    # Create a SELECT statement to query the row for the given steamid64 from the ck_playerrank table
    stmt = select(PlayerRank.steamid).\
        where(PlayerRank.steamid64 == steamid64)

    # Execute the SELECT statement and fetch the row
    with engine.connect() as conn:
        row = conn.execute(stmt).fetchone()

    # If no row is found, return None
    if row is None:
        return None

    # Extract the value of steamid from the row
    steamid = row[0]

    return steamid

def get_mostpoints():
    # Create a SELECT statement to query the row for the given steamid64 from the ck_playerrank table
    stmt = select(PlayerRank.__table__).\
    order_by(PlayerRank.points.desc()).\
    limit(1)
    
    # Execute the SELECT statement and fetch the row
    with engine.connect() as conn:
        row = conn.execute(stmt).fetchone()

    # If no row is found, return None
    if row is None:
        return None

    # Get the column names from the PlayerRank table
    column_names = PlayerRank.__table__.columns.keys()

    # Convert the row to a dictionary
    data = dict(zip(column_names, row))

    return data

def get_newestplayer():
    # Create a SELECT statement to query the row for the given steamid64 from the ck_playerrank table
    stmt = select(PlayerRank.__table__).\
    order_by(PlayerRank.joined.desc()).\
    limit(1)
    
    # Execute the SELECT statement and fetch the row
    with engine.connect() as conn:
        row = conn.execute(stmt).fetchone()

    # If no row is found, return None
    if row is None:
        return None

    # Get the column names from the PlayerRank table
    column_names = PlayerRank.__table__.columns.keys()

    # Convert the row to a dictionary
    data = dict(zip(column_names, row))

    return data

def get_mostcompletes():
    # Create a SELECT statement to query all rows from the ck_playerrank table
    stmt = select(PrInfo.mapname,func.count().label('record_count')).where((PrInfo.zonegroup == 0) &(PrInfo.runtime > 0)).group_by(PrInfo.mapname).order_by(func.count().desc()).limit(1)
   
    # Execute the SELECT statement and fetch all rows
    with engine.connect() as conn:
        row = conn.execute(stmt).fetchone()

    # If no row is found, return None
    if row is None:
        return None

    # Get the column names from the PlayerRank table
    column_names = PrInfo.__table__.columns.keys()

    # Convert the row to a dictionary
    data = dict(zip(column_names, row))

    return data

def get_incomplete():

    # Create a SELECT statement to query all rows from the ck_maptier table
    stmt = select(MapTier.mapname).where(not_(exists().where(PrInfo.mapname == MapTier.mapname))).limit(3)

    # Execute the SELECT statement and fetch all rows
    with engine.connect() as conn:
        rows = conn.execute(stmt).fetchall()

    # Get the column names from the MapTier table
    column_names = MapTier.__table__.columns.keys()

    # Convert the rows to a list of dictionaries
    data = [dict(zip(column_names, row)) for row in rows]

    return data

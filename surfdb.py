from sqlalchemy import create_engine, select, func
from surftimer import *
import configparser

CONFIG_PATH = 'config.ini'  
CONFIG = configparser.RawConfigParser()
CONFIG.read(CONFIG_PATH)

DB_HOST = str(CONFIG.get('surfdb', 'HOSTNAME'))
DB_USER = str(CONFIG.get('surfdb', 'USERNAME'))
DB_PASS = str(CONFIG.get('surfdb', 'PASSWORD'))
DB_NAME = str(CONFIG.get('surfdb', 'DB'))

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
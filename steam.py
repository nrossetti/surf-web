import requests
#import configparser
import os

#CONFIG_PATH = 'config.ini'  
#CONFIG = configparser.RawConfigParser()
#CONFIG.read(CONFIG_PATH)

API_KEY = os.environ.get('STEAM_API_KEY')
ADDRESS = os.environ.get('SERVER_IP')
PORT = os.environ.get('SERVER_PORT')
APP_ID = 730
IMG_DIR = os.environ.get('IMG_DIR')
#API_KEY = str(CONFIG.get('steam', 'STEAM_API_KEY'))
#ADDRESS = str(CONFIG.get('steam', 'SERVER_IP'))
#PORT = str(CONFIG.get('steam', 'SERVER_PORT'))
#APP_ID = 730  #csgo
#IMG_DIR = str(CONFIG.get('fastdl', 'IMG_DIR'))

def server_update():
    # Construct the URL to retrieve server information for the specified App ID
    url = f"https://api.steampowered.com/ISteamApps/GetServersAtAddress/v1/?addr={ADDRESS}:{PORT}&format=json&appid={APP_ID}&key={API_KEY}"

    # Make the API request and retrieve the server information
    response = requests.get(url)

    if response.status_code == 200:
        server_info = response.json()
    else:
        print(f"Error retrieving server information (status code {response.status_code})")
        return None

    # Construct the URL to retrieve server information for the specified server IP and port
    url = f"https://api.steampowered.com/IGameServersService/GetServerList/v1/?key={API_KEY}&filter=addr\{ADDRESS}:{PORT}"

    # Make the API request and retrieve the server information
    response = requests.get(url)

    if response.status_code == 200:
        server_info = response.json()["response"]["servers"][0]
        server_name = server_info['name']
        map_name = server_info['map']
        player_count = f"{server_info['players']}/{server_info['max_players']}"
        ip_address = server_info['addr']
        map = server_info['map']
        return {'server_name': server_name, 'map_name': map_name, 'player_count': player_count, 'ip_address': ip_address, 'map': map}
    else:
        print(f"Error retrieving server information (status code {response.status_code})")
        return None
    
def profile_url(steamid64):
    # retrieve player's Steam profile data
    response = requests.get(f'https://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key={API_KEY}&steamids={steamid64}')

    # parse the response to retrieve the player's profile picture URL
    data = response.json()['response']['players'][0]
    profile_picture_url = data['avatarfull']

    return profile_picture_url

def get_map_pic(mapname, bonus=0):
    path = IMG_DIR
    path += mapname
    if bonus > 0:
        path+='_b'+str(bonus)
    
    return path+'.jpg'
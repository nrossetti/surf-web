from flask import Flask, render_template,session, request
from steam import *
from surfdb import *

app = Flask(__name__)

@app.route('/')
def servers():
    server_info = server_update()
    if server_info is None:
        server_info = {'server_name': 'Server Offline', 'map_name': '', 'player_count': '', 'ip_address': '', 'map': ''}
    map_pic = get_map_pic(server_info['map'])
    return render_template('index.html', server_info=server_info, map_pic=map_pic)
    
@app.route('/players')
def players():
    data = get_players()
    mostpoints = get_mostpoints()
    newestplayer = get_newestplayer()
    numplayers = len(data)
    return render_template('players.html', data=data, mostpoints=mostpoints, newestplayer=newestplayer, numplayers=numplayers)

@app.route('/top')
def top():
    data = get_top()
    return render_template('top.html', data=data)

@app.route('/profile/<steamid64>')
def player_stats(steamid64):
    data = get_player(steamid64) 
    steamid=get_steamid(steamid64)
    data2 = get_playerrecs(steamid)
    steam_avatar = profile_url(steamid64)
    # render the player.html template with the player's data and profile picture URL
    return render_template('player-stats.html', data=data, data2=data2, profile_picture_url=steam_avatar)

@app.route('/latest')
def latest():
    data = get_latest()
    return render_template('latest.html', data=data)

@app.route('/maps')
def maps():
    data = get_maps()
    mostcompletes = get_mostcompletes()
    incomplete = get_incomplete()
    return render_template('maps.html', data=data, totalmaps=len(data), mostcompletes=mostcompletes, incomplete=incomplete)

@app.route('/map/<mapname>')
def map(mapname):
    data = get_maprec(mapname) 
    data2 = get_maptier(mapname)
    map_pic = get_map_pic(mapname)
    # render the player.html template with the player's data and profile picture URL
    return render_template('map.html', data=data, data2=data2, recordCount=len(data), map_pic=map_pic)


if __name__ == '__main__':
    app.run(host='0.0.0.0')

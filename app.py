from flask import Flask, render_template,session, request, jsonify
from steam import *
from surfdb import *

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

@app.route('/')
def servers():
# Get the IP address of the visitor
    ip_address = request.remote_addr
    
    # Check if the IP address has been seen before
    if ip_address not in session:
        session[ip_address] = True
        session['count'] = session.get('count', 0) + 1
        
    # Return the response
    print(f'This page has been viewed by {session["count"]} unique visitors.')

    server_info = server_update()
    if server_info is None:
        server_info = {'server_name': 'Server Offline', 'map_name': '', 'player_count': '', 'ip_address': '', 'map': ''}
    return render_template('index.html', server_info=server_info)
    
@app.route('/players')
def players():
    data = get_players()
    return render_template('players.html', data=data)

@app.route('/top')
def top():
    data = get_top()
    return render_template('top.html', data=data)

@app.route('/profile/<steamid64>')
def player_stats(steamid64):
    data = get_player(steamid64) 
    steam_avatar = profile_url(steamid64)
    # render the player.html template with the player's data and profile picture URL
    return render_template('player-stats.html', data=data, profile_picture_url=steam_avatar)

@app.route('/latest')
def latest():
    data = get_latest()
    return render_template('latest.html', data=data)

@app.route('/maps')
def maps():
    data = get_maps()
    return render_template('maps.html', data=data)

if __name__ == '__main__':
    app.run()

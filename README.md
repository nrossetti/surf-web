# Surf Web for CS:GO Surf Servers

![Logo](logo.png)

Surf Web is a Python Flask application developed by Nick "Chocolate Lasagna" for CS:GO surf server management. It serves as a web interface that provides valuable information about the server status, player statistics, and more.

## Features

- Real-time server status updates
- Player leaderboards and statistics
- Surf maps and world records
- Server announcements and news
- Player profiles and achievements
- Responsive and user-friendly interface

## Requirements

To run the Surf Web application, make sure you have the following requirements installed:

- Python 3.x
- Flask
- Flask-SocketIO
- CS:GO server with RCON access

## Installation

1. Clone the repository:

```git clone https://github.com/nick-chocolatel/surf-web.git```

2. Change into the project directory:

```cd surf-web```


3. Install the required dependencies:

```pip install -r requirements.txt```

4. Configure the application:

- Open the `config.py` file and modify the server settings according to your CS:GO surf server.
- Adjust any other necessary configurations in the file.

5. Run the application:
```python app.py```

6. Access the Surf Web application in your browser:
http://localhost:5000

## Usage

Once you have the Surf Web application up and running, you can access the various features provided by navigating through the user interface. Here are some of the key functionalities:

- **Server Status**: View real-time information about the server, such as the number of players, map rotation, and online/offline status.
- **Player Statistics**: Check out the leaderboards and track individual player stats, including playtime, completed maps, and top scores.
- **Surf Maps**: Browse through the available surf maps, view their difficulty ratings, and explore world records set by players.
- **Server Announcements**: Stay informed about the latest server news, events, and updates posted by the server administrators.
- **Player Profiles**: Create and customize your player profile, unlock achievements, and compete with other surfers on the server.

## Contributing

Contributions to Surf Web are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue on the [GitHub repository](https://github.com/nick-chocolatel/surf-web/issues).

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- The Flask framework: [Flask](https://flask.palletsprojects.com/)
- The Socket.IO library: [Flask-SocketIO](https://flask-socketio.readthedocs.io/)

Feel free to reach out if you have any questions or need further assistance. Happy surfing!

import threading
# Test threading daemon
#from threading import Timer

from keys import get_twitter_keys
from twython import Twython

from flask import Flask, render_template
from flask_socketio import SocketIO, emit

# Se crea la instancia global del objeto Flask
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
app.config['DEBUG'] = True

# socketio = SocketIO(app)
socketio = SocketIO(app, async_mode='eventlet')

# import test_twython2
from twython_streamer import MyStreamer
from twitter_api import get_twitter_api

# Para poder recibir los tweets en tiempo real
# Se crea una variable global para almacenar el streamer
twitter_stream = None


# Ruta por defecto de la página principal
@app.route('/')
def index():
	return render_template('base.html', async_mode=socketio.async_mode)


# Conexión del usuario
@socketio.

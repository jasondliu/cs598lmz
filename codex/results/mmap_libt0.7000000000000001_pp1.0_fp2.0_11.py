import mmap
import random
from datetime import datetime
from flask_cors import CORS
import simplejson as json
from flask import Flask, request, jsonify
from geopy.geocoders import Nominatim

from flask import render_template
from flask_socketio import SocketIO, emit

from geopy.distance import great_circle

from flask_cors import CORS



app = Flask(__name__)
CORS(app)
socketio = SocketIO(app, async_mode=None)

global pools
global pool_map
global pool_map_reverse
pools = []
pool_map = {}
pool_map_reverse = {}
global lat_long_pool_map
lat_long_pool_map = {}
global lat_long_pool_map_reverse
lat_long_pool_map_reverse = {}

def match_user(user):
    user_lat = user["lat"]
    user_long = user["long"]
    user_pool = user["pool"]
    print(user_lat)
    print(user_long)
   

import ctypes
import ctypes.util
import threading
import sqlite3
import time
import json
import os
from datetime import datetime
from flask import Flask, request, render_template, send_from_directory
from flask import jsonify
from flask import Response
from flask_cors import CORS
AC = ctypes.CDLL('libAC.so')


app = Flask(__name__, static_url_path='')
CORS(app)

def device_id_from_mac(mac):
    mac_array = mac.split(':')
    mac_val = 0
    for i in range(len(mac_array)):
        if mac_array[i] == '':
            mac_array[i] = '00'
        val = int(mac_array[i], 16)
        mac_val = mac_val << 8
        mac_val += val
    
    device_id = 0
    for i in range(len(mac_array)):
        val = mac_array[i]
        val = int(val, 16)
        device_id += val << (8*i)
    
    return device

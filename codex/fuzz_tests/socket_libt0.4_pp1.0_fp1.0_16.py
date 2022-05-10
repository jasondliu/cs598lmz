import socket
import sys
import time
import traceback

from flask import Flask, request, render_template, abort
from flask_socketio import SocketIO, emit

from pymodbus.client.sync import ModbusTcpClient

import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)
socketio = SocketIO(app)

#
#
#

def read_modbus(client, unit, address, count):
    result = client.read_holding_registers(address, count, unit=unit)
    if not result.isError():
        return result.registers
    else:
        logger.error("Modbus error: {}".format(result))
        return None

#
#
#

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/v1/<string:ip>/<int:unit>/<int:address>/<int:count>')


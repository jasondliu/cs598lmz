import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect("/home/pi/house.db")

from lib.log import setup_logging
from lib.util import get_client
from lib.lamp import lamp_on, lamp_off
from lib.lcd import LCD

from lib.database import Database
from lib.database import Event

logger = setup_logging()
logger.info("Starting...")

import time
from lib.lcd import LCD

import lib.mqtt_client as mqtt

from lib.mqtt_client import MqttClient

lcd = LCD()

lcd.set_line_one("Starting...")

client = get_client()

lcd.set_line_two("Client: {}".format(client))

client.publish("house/lcd/line1", "Starting...")
client.publish("house/lcd/line2", "Client: {}".format(client))

database = Database()


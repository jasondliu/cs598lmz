import ctypes
import ctypes.util
import threading
import sqlite3

from mqtt import Mqtt
from utils import get_configuration

from envirophat import weather, light, motion, leds

# total program length
wait_time_seconds = 3600

# mqtt config
mqtt_config = {
    'host': 'localhost',
    'port': '1883',
    'username': '',
    'password': '',
    'publish_topic': 'sensor/test/enviro',
    'qos': 2,
    'retain': False
}

# db config
db_config = {
    'database': 'enviro.db',
    'thread': False,
}

# update mqtt config
mqtt_config.update(get_configuration(section='mqtt'))

# update db config
db_config.update(get_configuration(section='database'))

# get db path

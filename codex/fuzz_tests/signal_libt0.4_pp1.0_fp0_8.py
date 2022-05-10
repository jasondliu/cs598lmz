import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import sys
import os
import datetime
import json
import time
import requests
import logging
import logging.handlers
import argparse
import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish

from influxdb import InfluxDBClient

#
#   Logging
#
LOG_FILENAME = "log/logger.log"
LOG_LEVEL = logging.INFO

logger = logging.getLogger(__name__)
logger.setLevel(LOG_LEVEL)
handler = logging.handlers.RotatingFileHandler(LOG_FILENAME, maxBytes=1048576, backupCount=5)
handler.setLevel(LOG_LEVEL)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

#
#   MQ

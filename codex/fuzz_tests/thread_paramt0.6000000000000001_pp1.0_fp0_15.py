import sys, threading
threading.Thread(target=lambda: sys.stdout.write("\n")).start()

import os
import time
import subprocess
import signal

import yaml
import json
import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish

import logging
log = logging.getLogger('root')

import pychromecast as pcc
import pychromecast.controllers.dashcast as dashcast

# TODO: 
# - handle errors (e.g. if the Chromecast is not available)
# - check if the Chromecast is already playing something
# - check if the Chromecast is already playing the stream
# - check if the Chromecast is in standby mode
# - check if the Chromecast is in idle mode
# - handle disconnections

class ChromecastController:
    def __init__(self, config):
        self.config = config

        self.client = mqtt.Client()
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.client.on_

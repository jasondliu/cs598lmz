import socket
import sys
import time
import threading
import os
import re
import json
import datetime
import logging
import logging.handlers
import signal

from collections import defaultdict

import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

import paho.mqtt.client as mqtt

# Disable insecure request warning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# Global variables
config = {}
logger = None

# MQTT client
mqtt_client = None

# MQTT publish queue
mqtt_queue = []

# MQTT queue lock
mqtt_queue_lock = threading.Lock()

# MQTT queue thread
mqtt_queue_thread = None

# MQTT queue thread stop flag
mqtt_queue_thread_stop = False

# MQTT queue thread event
mqtt_queue_thread_event = threading.Event()

# MQTT queue thread event
mqtt_queue_

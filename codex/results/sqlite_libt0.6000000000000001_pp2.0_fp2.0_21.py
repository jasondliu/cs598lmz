import ctypes
import ctypes.util
import threading
import sqlite3
import os
import os.path
import sys
import time
import datetime
import ConfigParser
import argparse
import logging
import logging.handlers
import json
import copy
import paho.mqtt.client as mqtt
import requests
import socket

#
# Global Data
#

# Version number
version = "0.1"

# Device name
deviceName = "pi-mote"

# Device type
deviceType = "Raspberry Pi"

# Device version
deviceVersion = "1"

# Device ID
deviceId = ""

# MQTT client
mqttClient = None

# MQTT client lock
mqttClientLock = threading.Lock()

# MQTT client online
mqttClientOnline = False

# MQTT client online lock
mqttClientOnlineLock = threading.Lock()

# MQTT client last will
mqttClientLastWill = None

# MQTT client last will lock
mqttClientLastWillLock = threading.Lock()

# MQTT broker

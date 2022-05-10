import ctypes
import ctypes.util
import threading
import sqlite3
import datetime
import sys
import os
import socket
import time
import json
import paho.mqtt.client as mqtt

#load shared library
libc = ctypes.CDLL(ctypes.util.find_library('c'))

#define constants
DEV_NAME = sys.argv[1]
MQTT_SERVER = "127.0.0.1"
USER = "root"
PASS = "root"

class Mqtt():
    def __init__(self):
        self.mqttc = mqtt.Client()
        self.mqttc.username_pw_set(USER, PASS)
        self.mqttc.connect(MQTT_SERVER, 1883)
        self.mqttc.loop_start()

    def publish(self, topic, payload):
        self.mqttc.publish(topic, payload, qos=0, retain=False)


class MetricsDB():
    def __init__(self,db_file):
        self.conn = sqlite3

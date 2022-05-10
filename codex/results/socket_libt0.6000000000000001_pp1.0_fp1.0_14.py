import socket
import pickle
import os.path
import sys
import threading
import time
import datetime
import paho.mqtt.client as mqtt

class Client:
    def __init__(self, name, port, host, mqtt_port, mqtt_host):
        self.name = name
        self.port = port
        self.host = host
        self.mqtt_port = mqtt_port
        self.mqtt_host = mqtt_host
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((host, port))
        self.mqtt_client = mqtt.Client()
        self.mqtt_client.connect(mqtt_host, mqtt_port)
        self.mqtt_client.on_message = self.on_message
        self.mqtt_client.subscribe(self.name)

    def on_message(self, client, userdata, message):
        print(

import select
import socket
import sys
import threading
import time
import uuid

import paho.mqtt.client as mqtt

from network import Network
from network_handler import NetworkHandler

from config import SERVER_PORT, SERVER_IP
from config import LOG_DIR

from config import LOGGER_NAME, LOGGER_LEVEL, LOGGER_FORMAT

from config import MQTT_SERVER_IP, MQTT_SERVER_PORT

from logger import Logger

class Server():

    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.clients = []
        self.client_addr = {}
        self.client_id = {}

        self.logger = Logger(LOGGER_NAME, LOGGER_LEVEL, LOGGER_FORMAT, LOG_DIR, True)
        self.logger.info("Server starting...")

        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


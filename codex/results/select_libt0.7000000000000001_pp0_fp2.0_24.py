import select
import sys
import time
import logging
import thread
import json
import signal
import sys
import socket
import rpyc
import os
import os.path
import math
import traceback

logging.basicConfig(filename="client.log", level=logging.INFO)

# Function to handle ctrl+c
def signal_handler(signal, frame):
    print 'You pressed Ctrl+C!'
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

class Client:
    def __init__(self, master_ip, master_port, client_ip, client_port, client_id):
        self.master_ip = master_ip
        self.master_port = master_port
        self.client_ip = client_ip
        self.client_port = client_port
        self.client_id = client_id

        logging.info("Client Initialized with Master Ip = " + str(self.master_ip) + " Master Port = " + str(self.master_port) + " Client I

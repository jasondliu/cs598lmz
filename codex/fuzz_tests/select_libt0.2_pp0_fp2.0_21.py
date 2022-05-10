import select
import socket
import sys
import time
import threading
import Queue

import paho.mqtt.client as mqtt

from config import *
from mqtt_client import *
from mqtt_server import *

# Constants

# Global variables

# Functions

def main():
    """
    Main function
    """
    # Create MQTT client
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(MQTT_HOST, MQTT_PORT, MQTT_KEEPALIVE_INTERVAL)

    # Create MQTT server
    server = MQTTServer(client)
    server.start()

    # Start MQTT client
    client.loop_start()

    # Wait for MQTT server to stop
    server.join()

    # Stop MQTT client
    client.loop_stop()

if __name__ == '__main__':
    main()

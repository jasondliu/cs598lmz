import select
import sys
import os
import time
import logging
import threading
import socket

import paho.mqtt.client as mqtt

from . import utils
from . import mqtt_client
from . import mqtt_server

logger = logging.getLogger(__name__)


def main():
    parser = argparse.ArgumentParser(description='MQTT Proxy')
    parser.add_argument('-v', '--verbose', action='store_true', help='verbose output')
    parser.add_argument('-l', '--log', type=str, help='log file')
    parser.add_argument('-c', '--config', type=str, help='config file')
    parser.add_argument('-d', '--daemon', action='store_true', help='run as daemon')
    parser.add_argument('-p', '--pidfile', type=str, help='pid file')

    args = parser.parse_args()

    if args.verbose:
        logging.basicConfig(level=logging.

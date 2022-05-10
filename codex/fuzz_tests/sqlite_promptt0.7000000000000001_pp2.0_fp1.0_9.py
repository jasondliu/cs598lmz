import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('test.db')
import sys
import os
import time
import random
import string
import datetime
import json
# Test json.loads(json.dumps({"a": "1", "b": 2}))
import argparse
# Test argparse.ArgumentParser().parse_args()
import traceback

# 3rd party
import requests
import paho.mqtt.client as mqtt

# Local
from HID import HID
from HID import Device as HIDDevice
from HID import Command as HIDCommand

from utility import *

#------------------------------------------------------------------------------
# Globals

#------------------------------------------------------------------------------
# Functions

#------------------------------------------------------------------------------
# Classes

#------------------------------------------------------------------------------
# Main
def main():
    print('HID device test')

    devices = HID.enumerate(0xffff, 0xffff)
    if not devices:
        print('No devices found')
        sys.exit(1)

    for dev in devices:
        print(dev)

        dev = HIDDevice()
        dev.open_path(path)
        dev.

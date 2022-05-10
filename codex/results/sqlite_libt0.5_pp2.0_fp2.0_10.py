import ctypes
import ctypes.util
import threading
import sqlite3
import json
import os
import sys
import time
import subprocess
from collections import defaultdict
from pprint import pprint
#import pdb

#pdb.set_trace()

class BLEEventHandler(object):
    def __init__(self, callback):
        self.callback = callback
        self.lock = threading.Lock()

    def __call__(self, device, event_type, event_data, user_data):
        with self.lock:
            self.callback(device, event_type, event_data, user_data)


class BLEAdapter(object):
    def __init__(self, adapter_name):
        self.adapter_name = adapter_name
        self.dbus = dbus.SystemBus()
        self.bluez_interface = "org.bluez"
        self.bluez_adapter_interface = self.bluez_interface + ".Adapter1"
        self.bluez_device_interface = self.bluez_interface + ".Device1"
        self.bluez_gatt_service_interface = self

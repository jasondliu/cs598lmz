import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect("share_memory.db")
import sys
import os
#sys.path.append("/home/pi/Desktop/drone/dronekit/lib/python2.7")
#from dronekit import connect
import time
import sys
from time import sleep
from dronekit import connect, VehicleMode

import os
import copy
import argparse
import json

def parse_vehicle_object(obj):
	"""
	Accepts a Vehicle Object obj, and returns a dictionary with the attributes we want.
	"""
	
	# Unpack the items we want
	dict = {}
	dict['location'] = copy.deepcopy(obj.location)
	dict['battery'] = {"voltage": obj.battery.voltage, "level": obj.battery.level, "current": obj.battery.current}
	dict['last_heartbeat'] = obj.last_heartbeat
	dict['last_seen'] = obj.last_seen
	dict['armed'] = obj.armed
	dict['rssi'] = obj.gps_0.eph
	dict['heading'] =

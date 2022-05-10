import mmap
import os
import re
import shutil
import signal
import sys
import time
import datetime
import math
import sqlite3

import pigpio
import serial
import struct
import threading
import traceback

import config

sys.path.append(config.APP_PATH)

from db import db
import connection
import data
import edoors
import gpsd_client
import log
import mavlink_reader
import mavlink_writer
import mavutil
import messaging
import mission
import mod_global
import params
import qgc
import rf_server
import rf_client
import signals
import util
import watchdog

BINDING_FILE_PREFIX = "binding_"
BINDING_FILE_EXT = ".json"

class MavlinkMain(object):
	def __init__(self):
		self.args = None
		self.fds = {}
		self.mavlink_writer = None

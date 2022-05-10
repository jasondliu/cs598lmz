import ctypes
import ctypes.util
import threading
import sqlite3
import time
from multiprocessing import Process
from enum import Enum

import pymavlink.mavutil as mavutil
from pymavlink import mavwp

from dronekit import mavlink
from dronekit import VehicleMode, LocationGlobalRelative, LocationGlobal, LocationLocal, Command
from dronekit import connect
from dronekit.console import set_logfile, enable_flush
from dronekit.lib import VehicleMode, LocationGlobalRelative, LocationGlobal, LocationLocal, Command, Vehicle
from dronekit.lib import VehicleMode, LocationGlobal, LocationLocal, LocationGlobalRelative


#load some mysql
import mysql.connector
from mysql.connector import errorcode

import subprocess

from message import Message

class MysqlManager:

	def __init__(self):
		#Get the configs
		#TODO: Read the username and password from config
		import config
		username = config.username
		password = config.password
		self.conn = mysql.connector.connect(user=username, password=password, host='localhost',

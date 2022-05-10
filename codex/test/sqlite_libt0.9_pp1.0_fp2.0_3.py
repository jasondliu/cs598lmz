import ctypes
import ctypes.util
import threading
import sqlite3
import json
import os
import sys

class TempSensor:
	def __init__(self, path):
		assert len(path) == 11
		assert path.endswith('.db')
		assert path.startswith('/sys/bus/w1/devices/')
		self.path = path
		self.name = path[21:-3]

	def IsAvailable(self):
		return os.path.isfile(self.path)
	
	def GetValue(self):
		conn = sqlite3.connect(self.path)
		cursor = conn.cursor()

		cursor.execute('select "type", value from sensors')
		row = cursor.fetchone()
		assert row[0] == 'temperature_input'
		temp = row[1]/1000.0
		cursor.close()

		return temp

	def Read(self):
		res = {"Name": self.name, "Temperature": self.GetValue()}
		return res



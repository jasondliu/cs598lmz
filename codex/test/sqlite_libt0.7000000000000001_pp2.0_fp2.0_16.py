import ctypes
import ctypes.util
import threading
import sqlite3
import time

class DHT22(object):
    def __init__(self, sensorId, pin):
        self.sensorId = sensorId
        self.pin = pin
        self.sensor_active = False
        self.sensor_last_active = 0
        self.sensor_last_active_epoch = 0
        self.last_temperature = 0
        self.last_humidity = 0
        self.last_update_epoch = 0
        self.last_update_time = ""
        self.error = False
        self.error_message = "No error."
        
        self.lib_path = find_library('dht22')
        self.lib = ctypes.CDLL(self.lib_path)
        
        self.lib.readDHT22.restype = ctypes.c_int
        self.lib.readDHT22.argtypes = [ctypes.c_int]
        
        self.lib.getHumidity.restype = ctypes.c_float

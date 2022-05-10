import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('mytest.db') - can use instead of below
import os.path


class MOTIONSensorThread(threading.Thread):
    def __init__(self, databaseFileName):
        threading.Thread.__init__(self)
        self.sensorLib = ctypes.CDLL(ctypes.util.find_library("wiringPi"))
        self.sensorLib.pinMode(7, 0)
        self.sensorLib.wiringPiSetupSys()
        self.sensorLib.pullUpDnControl(7, 2)
        self.sensorLib.wiringPiISR(7, 2, self.motionDetected)
        self.is_motion = False
        self.motion_start_time = None
        self.motion_end_time = None
        self.is_door_open = False
        self.door_open_start_time = None
        self.door_open_end_time = None
        self.update_start_time = None
        self.is_updating = False

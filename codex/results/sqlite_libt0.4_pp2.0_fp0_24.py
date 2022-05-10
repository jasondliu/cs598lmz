import ctypes
import ctypes.util
import threading
import sqlite3
import time

class Device(object):
    def __init__(self, device_id, device_type, device_number, device_name, device_info, device_status, device_data):
        self.device_id = device_id
        self.device_type = device_type
        self.device_number = device_number
        self.device_name = device_name
        self.device_info = device_info
        self.device_status = device_status
        self.device_data = device_data


class DeviceManager(object):
    def __init__(self):
        self.devices = []
        self.devices_lock = threading.Lock()

        self.device_types = ['switch', 'sensor', 'actuator']

    def add(self, device):
        self.devices_lock.acquire()
        self.devices.append(device)
        self.devices_lock.release()

    def remove(self, device_id):
        self.devices_lock.acquire()
        for i in range(len(self.devices

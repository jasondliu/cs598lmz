import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('testdb.sqlite3', check_same_thread=False)
import os
import sys
import datetime

# TODO: Add a way to call this function without having to import this whole
#       module.
def get_vendor_id(device_path):
    """
    Return the vendor ID of the device at the given path.
    """
    return int(device_path.split('/')[-1].split('-')[0], 16)

def get_device_id(device_path):
    """
    Return the device ID of the device at the given path.
    """
    return int(device_path.split('/')[-1].split('-')[1], 16)

def get_serial_number(device_path):
    """
    Return the serial number of the device at the given path.
    """
    return device_path.split('/')[-1].split('-')[2]

def get_usb_devices():
    """
    Return a list of all USB devices connected to the computer.
    """
    return

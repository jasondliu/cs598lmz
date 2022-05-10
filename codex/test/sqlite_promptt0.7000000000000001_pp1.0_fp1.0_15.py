import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect
#print(sqlite3.connect('data.db'))

import time
import Queue

from lib.smbus2 import SMBus
from lib.smbus2 import i2c_msg
from lib.smbus2 import i2c_rdwr
from lib.smbus2 import I2C_M_RD
from lib.smbus2 import I2C_M_TEN
from lib.smbus2 import I2C_M_WR

from lib.DS3231 import DS3231
from lib.INA219 import INA219


def get_rtc():
    """Get the current time from the RTC"""
    rtc = DS3231(1)
    return rtc.datetime()


def get_energy():
    """Get the current energy usage"""
    ina219 = INA219(1, 0x40)
    return ina219.current()


def get_energy_start():
    """Get the energy usage at the start of the day"""
    ina219 = INA219(1, 0x40)

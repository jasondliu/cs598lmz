import ctypes
import ctypes.util
import threading
import sqlite3

NS = 1000000000
UDISKS_BUS_NAME = 'org.freedesktop.UDisks'
UDISKS_DEVICE_INTERFACE = 'org.freedesktop.UDisks.Device'
UDISKS_MANAGER_INTERFACE = 'org.freedesktop.UDisks.Manager'
UDISKS_PATH_ROOT = '/org/freedesktop/UDisks'
UDISKS_PATH_OBJECTS = '/org/freedesktop/UDisks/devices'

GUDEV_AMEDIA_CATEGORY = 'Drive'
GUDEV_DATA_PREPENDED_ROOT = '1'
GUDEV_DEVICE_MANAGER = 'org.freedesktop.UDisks'
GUDEV_DEVICE_NAME = 'UDisks'
GUDEV_DEVICE_OBJECT = 'org.freedesktop.UDisks'
GUDEV_DEVICE_TYPE = 'drive'
GUDEV_DEVICE_UUID = 'UUID'
GUDEV_DEVICE_VENDOR =

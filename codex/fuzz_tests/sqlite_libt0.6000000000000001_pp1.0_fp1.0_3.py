import ctypes
import ctypes.util
import threading
import sqlite3
import time
import logging

import dbus
import dbus.service
import dbus.mainloop.glib
from gi.repository import GObject

from . import const
from . import dialog
from . import models
from . import network
from . import utils

_dbus_name = 'org.freedesktop.NetworkManager'
_dbus_path = '/org/freedesktop/NetworkManager'
_dbus_interface = 'org.freedesktop.NetworkManager'

_dbus_device_interface = 'org.freedesktop.NetworkManager.Device'
_dbus_device_wireless_interface = 'org.freedesktop.NetworkManager.Device.Wireless'
_dbus_access_point_interface = 'org.freedesktop.NetworkManager.AccessPoint'
_dbus_settings_interface = 'org.freedesktop.NetworkManager.Settings'
_dbus_settings_connection_interface = 'org.freedesktop.NetworkManager.Settings.Connection'
_dbus_settings_connection_active_

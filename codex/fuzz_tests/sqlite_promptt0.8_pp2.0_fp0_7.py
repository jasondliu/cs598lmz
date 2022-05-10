import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect("/share/Fritz.Box_Telefonbuch.xml")
import time
import logging

# GObject Setup
GObject.threads_init()

# Avahi setup
DBUS_NAME = 'org.freedesktop.Avahi'
DBUS_INTERFACE_SERVER = DBUS_NAME + '.Server'
DBUS_PATH_SERVER = '/'

AVAHI_IF_UNSPEC = -1
AVAHI_PROTO_UNSPEC = -1

# Avahi browser setup
DBUS_INTERFACE_ENTRY_GROUP = DBUS_NAME + '.EntryGroup'
DBUS_PATH_ENTRY_GROUP = '/EntryGroup'
DBUS_INTERFACE_DOMAIN_BROWSER = DBUS_NAME + '.DomainBrowser'
DBUS_INTERFACE_SERVICE_BROWSER = DBUS_NAME + '.ServiceBrowser'
DBUS_INTERFACE_SERVICE_TYPE_BROWSER = DBUS_NAME + '.ServiceTypeBrowser'

AVAHI_LOOKUP_RESULT_CACHED = 1
AVAHI_L

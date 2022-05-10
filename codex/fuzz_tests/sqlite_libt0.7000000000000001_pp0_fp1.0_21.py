import ctypes
import ctypes.util
import threading
import sqlite3
import os
import time

# TODO: Refactor as a class to create a new object for each gnome-keyring
#   unlocking request

# TODO: Use g_dbus_* functions to communicate with gnome-keyring
#   (http://library.gnome.org/devel/glib/stable/glib-D-Bus.html)

# TODO: Investigate using g_bus_watch_name() with G_BUS_NAME_WATCHER_FLAGS_NONE
#   and g_bus_unwatch_name()
#   (http://library.gnome.org/devel/glib/stable/glib-D-Bus.html)

# TODO: Make this a DBUS service

# TODO: Add support for custom gnome-keyring-daemon location

KEYRING_DAEMON_PID_FILE = '/var/run/user/%d/keyring/control'
KEYRING_DAEMON_SOCKET_FILE = '/run/user/%d/keyring/socket'
KEYRING_

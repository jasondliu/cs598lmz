import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('/var/lib/dbus/machine-id')
import gobject
import gio

def gnome_session_is_running():
    bus = dbus.SessionBus()
    try:
        bus.get_object('org.gnome.SessionManager',
                       '/org/gnome/SessionManager')
    except dbus.DBusException:
        return False
    else:
        return True

def logind_is_running():
    bus = dbus.SystemBus()
    try:
        bus.get_object('org.freedesktop.login1',
                       '/org/freedesktop/login1')
    except dbus.DBusException:
        return False
    else:
        return True

class LockScreen(object):
    def __init__(self):
        self.is_lock = False
        self.is_lock_gnomes = False
        self.is_lock_logind = False
        self.is_lock_gsettings = False
        self.install_gnome()
        self.install_logind()
       

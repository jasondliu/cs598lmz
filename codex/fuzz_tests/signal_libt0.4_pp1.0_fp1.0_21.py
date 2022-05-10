import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

import os
import sys
import logging
import logging.handlers
import time
import traceback

import dbus
import dbus.service
import dbus.mainloop.glib
import gobject

#-------------------------------------------------------------------------------

class DBusService(dbus.service.Object):
    def __init__(self, bus_name, object_path):
        dbus.service.Object.__init__(self, bus_name, object_path)

    @dbus.service.method('org.freedesktop.DBus.Introspectable')
    def Introspect(self):
        return dbus.service.Object.Introspect(self, self.__dbus_object_path__)

    @dbus.service.method(dbus_interface='org.freedesktop.DBus.Peer',
                         in_signature='', out_signature='')
    def Ping(self):
        pass

    @dbus.service.method(dbus_interface='org

import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

from gi.repository import Gtk, Gdk, GLib
from gi.repository import GObject
from gi.repository import AppIndicator3 as appindicator
from gi.repository import Notify

from dbus.mainloop.glib import DBusGMainLoop
from dbus.exceptions import DBusException
import dbus

import os
import re
import time
import threading

# Icons dir
if getattr(sys, 'frozen', False):
    app_dir = os.path.dirname(sys.executable)
else:
    app_dir = os.path.dirname(os.path.realpath(__file__))

ICON_DIR = os.path.join(app_dir, 'icons')

# DBus services
BLUEZ_SERVICE_NAME = 'org.bluez'
BLUEZ_ADAPTER_INTERFACE = 'org.bluez.Adapter1'
BLUEZ_DEVICE

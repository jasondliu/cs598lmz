import ctypes
import ctypes.util
import threading
import sqlite3
import time
import re

import dbus.service
import dbus.mainloop.glib

try:
    from gi.repository import GObject
except ImportError:
    import gobject as GObject

from . import config

from . import util
from . import const

from . import log
from .log import logger

# =============================================================================
#
# =============================================================================

class PidginDBus(dbus.service.Object):
    DBUS_INTERFACE = 'im.pidgin.purple.PurpleInterface'
    DBUS_PATH = '/im/pidgin/purple/PurpleObject'
    def __init__(self, conn=None, object_path=None, bus=None):
        if not object_path:
            object_path = self.DBUS_PATH
        if not bus:
            bus = dbus.SessionBus()
        dbus.service.Object.__init__(self, bus, object_path)
        self.__conn = conn

    # =========================================================================
    #
    # =========================================================================

    @dbus

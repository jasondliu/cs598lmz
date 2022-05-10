import gc, weakref
import os
import sys
import time
import traceback

import gobject
import gtk

import awn
import cairo
import xcursor

import awn.extras

from awn.extras import _, __version__

try:
    import dbus
    from dbus.mainloop.glib import DBusGMainLoop
    DBusGMainLoop(set_as_default=True)
    session_bus = dbus.SessionBus()
    import dbus.service
    from dbus.exceptions import DBusException
except ImportError:
    pass

try:
    import pynotify
except ImportError:
    pass

import awn.extras.__init__

def _(text):
    return text

def _get_icon_path(name):
    return awn.extras.__init__.__file__.replace(".pyc", ".py").replace(".pyo", ".py").replace("__init__.py", "icons/%s.png" % name)

def _get_icon_p

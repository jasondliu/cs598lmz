import ctypes
import ctypes.util
import threading
import sqlite3
import datetime

try:
    import dbus
    import dbus.service
    import dbus.glib
    from dbus.mainloop.glib import DBusGMainLoop
except ImportError:
    dbus = None

from . import util
from . import sync
from . import media
from . import playlist
from . import library

from .util import log


def get_default_pulse_sink():
    try:
        import pulsectl
    except ImportError:
        return None

    pulse = pulsectl.Pulse('mps-youtube')
    sinks = pulse.sink_list()
    for sink in sinks:
        if sink.name == 'alsa_output.pci-0000_00_1b.0.analog-stereo':
            return sink.index

    return None


class Config(object):
    def __init__(self, path):
        self.path = path
        self.db = sqlite3.connect(path)

        with self.db:
            self.db.execute('''CREATE TABLE

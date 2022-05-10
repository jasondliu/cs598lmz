import weakref
import threading

from PyQt5 import QtCore
from PyQt5.QtCore import Qt, QObject
from PyQt5.QtNetwork import QAbstractSocket



_half_delays = {}
_sock_to_timestamp = weakref.WeakKeyDictionary()
DEFAULT_HALF_CLOSE_DELAY = 15.0
DEFAULT_OUTPUT_BUFFER_SIZE = 16 * 1024
DEFAULT_PACKET_SIZE = 1e6
VERSION = '1.0'



def _callback(self, event, *args):
    event = self._fix_event(event)
    events = self.events[event]
    for (event, callback) in events:
        callback(*args)



def add_callback(self, event, callback):
    try:
        event_ref = self._EVENTS[event]
    except KeyError as e:
        raise ValueError('Unsupported event %s.' % event) from e
    else:
        if event_ref is self.HUP:
            self.events

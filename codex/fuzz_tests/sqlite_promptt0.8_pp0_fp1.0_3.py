import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect('test.db')

# TODO
# when a window is closed, it should be removed from window list
# dispatch all signals to all windows
# add signals for move and resize
# list all windows
# 

application = None

#
#
#
class GLibSignalEmitter(object):
    """This class implements a method to emit signals.  A signal is essentially
    a callback that can be registered and unregistered with a particular
    signal.  A signal is emitted by calling the emit() class method, which
    invokes the registered callbacks.  The callbacks are invoked in the order
    in which they were registered.
    """

    def __init__(self):
        self._signals = {}

    def connect(self, signal, callback):
        """Connect a callback to a signal."""
        if signal not in self._signals:
            self._signals[signal] = []
        if callback not in self._signals[signal]:
            self._signals[signal].append(callback)

    def disconnect(self, signal, callback):
        """Dis

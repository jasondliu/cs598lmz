import sys, threading
threading.Thread(target=lambda: sys.stdout.write("test\n")).start()

# If a thread doesn't need much python-level state, then it can be run
# more simply using the threading.Thread.run() method.  This invokes the
# callable object passed to the object's constructor with no arguments.
# The following subclasses the Thread class to show this, and also how
# a thread can be stopped through the use of a threading.Event object.

import threading

class StoppableThread(threading.Thread):
    """Thread class with a stop() method.  The thread itself has to check
    regularly for the stopped() condition."""

    def __init__(self, *args, **kwargs):
        super(StoppableThread, self).__init__(*args, **kwargs)
        self._stop = threading.Event()

    def stop(self):
        self._stop.set()

    def stopped(self):
        return self._stop.isSet()

# The following is a trivial application of the StoppableThread class.

import time
import random


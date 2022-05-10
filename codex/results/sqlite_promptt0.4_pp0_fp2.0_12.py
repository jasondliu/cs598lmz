import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect
import os
import time

libc = ctypes.CDLL(ctypes.util.find_library('c'))

# From http://stackoverflow.com/questions/14207708/io-error-errno-4-interrupted-function-call-python
def c_is_interrupted():
    return bool(libc.feof(libc.stdin))

# From http://stackoverflow.com/questions/1335507/keyboard-input-with-timeout-in-python
class KeyboardInput(threading.Thread):
    """Gets keyboard input, prints it to the screen, and stores it in a
    variable
    """
    def __init__(self, timeout=0.1):
        super(KeyboardInput, self).__init__()
        self.timeout = timeout
        self.input = None
        self.daemon = True
        self.start()

    def run(self):
        self.input = raw_input()

    def get_input(self):
        self.join(self.timeout)
        return self.input


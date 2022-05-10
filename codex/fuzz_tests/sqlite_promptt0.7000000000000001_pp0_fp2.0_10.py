import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(":memory:")

class XBee:
    def __init__(self, port=None, baudrate=None, callback=None):
        xbee_lib = ctypes.CDLL(ctypes.util.find_library("xbee"))
        self.xbee = xbee_lib.xbee_new()

        self._callback = None
        self.callback = callback

        self._thread = threading.Thread(target=self._recv_thread)
        self._thread.setDaemon(True)
        self._thread.start()

        if port:
            self.open(port, baudrate)

    def __del__(self):
        self.close()

    def _recv_thread(self):
        while True:
            xbee_lib.xbee_recv(self.xbee)

    @property
    def callback(self):
        return self._callback

    @callback.setter
    def callback(self, value):
        if self._callback:
            xbee_lib.xbee_conCallbackSet(self.xbee,

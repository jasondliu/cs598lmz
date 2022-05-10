import ctypes
import ctypes.util
import threading
import sqlite3
# Test sqlite3.connect(":memory:")


class SPIConfig(ctypes.Structure):
    _fields_ = [
        ("baud", ctypes.c_uint),
        ("cpha", ctypes.c_uint),
        ("cpol", ctypes.c_uint),
        ("csna_high", ctypes.c_uint),
    ]

    def __init__(self, baud, cpha, cpol, csna_high):
        super().__init__(baud, cpha, cpol, csna_high)

    def __repr__(self):
        return ("SPIConfig(baud = %r, cpha = %r, cpol = %r, csna_high = %r)" %
                (self.baud, self.cpha, self.cpol, self.csna_high))


class SPI():

    class SPILock(threading.RLock):

        def __init__(self, spi):
            super().__init__()
            self._spi = spi


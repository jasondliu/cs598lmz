import select
import sys
import time
import fcntl

# try:
#     from . import core
# except ImportError:
#     import core


class Serial(object):
    """Serial port base class

    This class is meant to be subclassed to provide an interface to the
    specific hardware.
    """
    def __init__(self, port, baudrate=9600, timeout=1,
                 bytesize=8, parity='N', stopbits=1, xonxoff=0, rtscts=0):
        """Initialize comm port object"""
        self._port = port
        self._is_open = False
        self._baudrate = baudrate
        self._bytesize = bytesize
        self._parity   = parity
        self._stopbits = stopbits
        self._xonxoff  = xonxoff
        self._rtscts   = rtscts
        self._timeout  = timeout

        # Precalculate byte sizes for later use
        if bytesize == 5:
            self._byte_size = 1
        el

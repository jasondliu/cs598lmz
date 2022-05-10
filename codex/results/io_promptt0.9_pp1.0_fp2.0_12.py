import io
# Test io.RawIOBase with rawio.RawIOBase.
import rawio
# Test io.RawIOBase with io.BufferedIOBase.
import buffered


import threading
import logging
import sys


try:
    import resource
    has_resource_module = True
except ImportError:
    has_resource_module = False


logger = logging.getLogger('example')


# Reads a single byte and echos it.
class RBSimpleReader(object):

    def __init__(self):
        self._lock = threading.Lock()
        self._data = None

    def read(self, size):
        """RBSimpleReader.read"""
        logger.debug('read(%d)', size)
        with self._lock:
            res = self._data
            self._data = None
        logger.debug('data=%r', res)
        return res or b''

    def write(self, data):
        """Writes a single byte."""
        logger.debug('write(%r)', data)
        with self._lock:
           

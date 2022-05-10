import select
import sys
import logging
import time
import threading

from . import util
from . import constants
from . import exceptions
from . import messages
from . import devices
from . import usb1
from . import usb

log = logging.getLogger(__name__)

class Usb1Device(devices.Device):
    """
    A libusb1-based USB device.
    """
    def _writeInterrupt(self, endpoint, data):
        log.debug("Writing interrupt data to endpoint {0:#04x}: {1!r}".format(endpoint, data))
        self.handle.interruptWrite(endpoint, data, self.timeout)
    
    def _readInterrupt(self, endpoint, length):
        log.debug("Reading interrupt data from endpoint {0:#04x} length {1}".format(endpoint, length))
        return self.handle.interruptRead(endpoint, length, self.timeout)
    

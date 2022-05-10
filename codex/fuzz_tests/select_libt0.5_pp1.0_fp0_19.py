import select
import sys
import time

import numpy as np

from . import constants
from . import util
from . import protocol

class USBRaw(object):
    """
    This class is used to send and receive raw USB data.
    """
    def __init__(self, usb_device):
        self._usb_device = usb_device
        self._usb_device.set_configuration()
        self._usb_device.claim_interface(0)
        self._usb_device.set_interface_altsetting(0, 0)
        self._usb_device.set_interface_altsetting(0, 1)
        self._usb_device.set_interface_altsetting(0, 2)
        self._usb_device.set_interface_altsetting(0, 3)
        self._usb_device.set_interface_altsetting(0, 4)
        self._usb_device.set_interface_altsetting(0, 5)
        self._usb_device.set_interface_altsetting(0, 6)
        self._usb_device

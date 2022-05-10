import weakref
import os
from gi.repository import GLib

from . import settings
from .udisks2 import UDisks2
from .enums import DeviceHandlerState, DeviceHandlerError
from .devicehandler import DeviceHandler
from .exceptions import DeviceHandlerErrorNotFound
from .utils import force_utf8
from .device import Device, LUKSDevice, FSLUKSDevice, EncryptedDevice
from .exceptions import DeviceError, DeviceErrorNotFound


class DeviceManager:
    """
    This class manages the devices currently available. This includes
    devices that are not currently connected, too.
    """

    def __init__(self, loop, udisks2: UDisks2, settings: settings.Settings):
        logger.debug("init class")
        self.loop = loop
        self.udisks2 = udisks2
        self.settings = settings

        self.devices = {}
        self.new_devices = {}

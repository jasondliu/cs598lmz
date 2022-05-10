import select
import signal
import sys
import time

from pyzwave.libopenzwave import PyManager
from pyzwave.message import Message

from . import controller
from . import device
from . import options
from . import protocol

LOGGER = logging.getLogger('pyzwave')


class ZWave(PyManager):
    """ZWave controller"""

    def __init__(self, device):
        """Create the ZWave controller.

        :param device: ZWave controller device
        :type device: str
        """
        self.device = device
        self.options = options.Options(device)

        super(ZWave, self).__init__(self.options)

        # Setup the controller
        self.controller = controller.Controller(self, self.options)
        self.controller.start()

        # Setup the protocol
        self.protocol = protocol.Protocol(self, self.device)
        self.protocol.start()

        # Setup the device information
        self.device_info = device.DeviceInfo(self)

        # Setup the devices
        self.

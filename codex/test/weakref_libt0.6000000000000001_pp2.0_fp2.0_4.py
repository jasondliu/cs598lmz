import weakref

from .abstract import *
from . import errors

class Connection(AbstractConnection):
    """Concrete connection to a device"""

    def __init__(self, device):
        super(Connection, self).__init__(device)
        self._device = weakref.ref(device)
        self._logger = logging.getLogger('maggma.connection.Connection')

    def send(self, command, args=None):
        """Send a command to the device"""
        self._logger.debug("Sending command: {}".format(command))
        try:
            self._device().send(command, args=args)
        except errors.DeviceError as e:
            self._logger.error("Device error: {}".format(e))
            raise ConnectionError("Device error: {}".format(e))
        except errors.ProtocolError as e:
            self._logger.error("Protocol error: {}".format(e))
            raise ConnectionError("Protocol error: {}".format(e))
        except errors.InterfaceError as e:
            self._logger

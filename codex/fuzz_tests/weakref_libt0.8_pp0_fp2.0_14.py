import weakref

from blivet.devicelibs import crypto

from blivet.util import run_program
from blivet.size import Size

import logging
log = logging.getLogger("blivet")

class LUKSError(Exception):
    pass

class LUKS(object):
    """
    A factory for a key-loaded LUKS device.
    """

    _type = "luks"
    _formatterClass = "crypto"
    _formatUUIDAttr = "uuid"

    def __init__(self, device, keyFile=None):
        """
        :param device: the device that is or contains a LUKS device
        :type device: :class:`~.devices.StorageDevice`
        :keyword key_file: the path to the file containing the key to unlock
        the LUKS device
        :type key_file: str
        """
        self._device = device
        self._keyFile = keyFile

    @property
    def status(self):
        """
        The device's status

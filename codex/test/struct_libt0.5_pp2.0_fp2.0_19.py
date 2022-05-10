import _struct

from . import base
from . import exceptions
from . import helpers


class Device(base.Device):
    """
    Represents a single device connected to the system.
    """

    def __init__(self, device_id, device_handle, device_info):
        super().__init__(device_id, device_handle, device_info)
        self.device_type = device_info.get('type')
        self.device_name = device_info.get('name')

    def __repr__(self):
        return "<{0.__module__}.{0.__name__} object at {1:#x} (id={2}, type={3}, name={4!r})>".format(
            type(self), id(self), self.device_id, self.device_type, self.device_name)

    @property
    def is_keyboard(self):
        """
        Returns ``True`` if this device is a keyboard.
        """
        return self.device_type == 'KEYBOARD'


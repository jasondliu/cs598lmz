import weakref

from . import _util
from . import _types
from . import _wrapper
from . import _wrapper_util

_logger = _util.get_logger(__name__)


def _get_device_list(device_type):
    """Get a list of devices of the given type.

    Args:
        device_type (str): The type of device to get.

    Returns:
        list[:class:`Device`]: A list of devices of the given type.
    """
    devices = []
    for device_id in range(_wrapper.get_device_count(device_type)):
        device = _wrapper.get_device(device_type, device_id)
        if device is None:
            _logger.warning(
                "Failed to get device of type %s with ID %d", device_type, device_id)
            continue
        devices.append(Device(device_type, device))
    return devices


class Device(object):
    """A device that can be used for inference.

    Args:
        device_type

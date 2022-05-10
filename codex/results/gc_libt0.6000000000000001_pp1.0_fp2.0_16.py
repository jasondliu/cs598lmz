import gc, weakref
from gc import get_objects
from pympler import asizeof
from sys import getsizeof as getsize
from collections import OrderedDict

from .raw_data import RawData
from .raw_event import RawEvent
from .raw_channel import RawChannel
from .raw_header import RawHeader


class RawGroup(object):
    """
    The RawGroup is the base class for all raw data objects.

    The RawGroup class is the base class for all raw data objects. It is not
    intended to be used directly.

    Parameters
    ----------
    raw_data : RawData, optional
        RawData object to which the RawGroup belongs.
    name : str, optional
        Name of the RawGroup.
    """
    def __init__(self, raw_data=None, name=None):
        self._raw_data = None
        self._name = None
        self._parent = None
        self._children = OrderedDict()
        self._locked = False

        if raw_data is not None:
            self.set_raw_data(raw_data

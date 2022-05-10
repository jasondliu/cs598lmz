import _struct
import time
import os
import sys
import math

if sys.version_info[0] == 2:
    import ConfigParser as configparser
else:
    import configparser


class _PyHID(object):
    """
    This class is the base class for all PyHID devices. It should not be
    instantiated directly.
    """

    _DEFAULT_CONFIG = {
        'vendor_id': 0x0,
        'product_id': 0x0,
        'usage_page': 0x0,
        'usage': 0x0,
        'interface': 0x0,
        'path': '',
        'serial': ''
    }

    def __init__(self, config):
        """
        Constructor for PyHID object.

        :param config: The configuration to use.
        :type config: dict
        """

        #: The device path
        self.path = config['path']

        #: The USB vendor ID
        self.vendor_id = config['vendor_id']

        #: The USB product ID

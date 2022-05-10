import select
import fcntl
import sys
import time
import atexit
import logging

from itertools import chain
from collections import namedtuple

import pyudev

try:
    from sarge import run, Capture
except ImportError:
    raise ImportError("You need to install the sarge package to use this module.")

# TODO create as class and sent over as arg
log = logging.getLogger(__name__)


class UdevWatcher(object):
    def __init__(self, *udev_enums, ensure_rules=False, timeout=10,
                 logger_name="UdevWatcher", *args, **kwargs):
        """
        :param udev_enums: List of udev enum to wait for
        :type udev_enums: list of str
        :param ensure_rules: If True, will make sure the udev rules are in place
        :type ensure_rules: bool
        :param timeout: Timeout in seconds to wait for udev events
        :type timeout: int
        """
        self.udev_en

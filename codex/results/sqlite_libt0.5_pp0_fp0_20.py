import ctypes
import ctypes.util
import threading
import sqlite3
from sqlite3 import Error
import time

from . import _libvmi
from . import _libvmi_extra
from . import utils
from . import constants
from .constants import *
from .exceptions import LibvmiError
from . import x86
from . import x86_constants
from .x86_constants import *
from . import arm
from . import arm_constants
from .arm_constants import *
from . import arm64
from . import arm64_constants
from .arm64_constants import *


class Libvmi(object):
    """
    Libvmi class.

    This class is a Python wrapper around libvmi.
    """

    def __init__(self, name=None, config_file=None, flags=None):
        """
        Initialize Libvmi, either by name or config_file.

        :param name: Name of the VM to attach to.
        :param config_file: Path to the config file.
        :param flags: Flags to be used for initialization.
        """
        self._v

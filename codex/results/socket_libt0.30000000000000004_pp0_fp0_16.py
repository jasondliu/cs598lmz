import socket
import struct
import sys
import time

from . import common
from . import config
from . import errors
from . import log
from . import net
from . import nvram
from . import util


def _get_nvram_key(key):
    """Get a key from NVRAM."""
    if not nvram.is_supported():
        return None
    return nvram.get_value(key)


def _set_nvram_key(key, value):
    """Set a key in NVRAM."""
    if not nvram.is_supported():
        return
    nvram.set_value(key, value)


def _get_nvram_key_or_default(key, default):
    """Get a key from NVRAM, or a default value if the key is not set."""
    if not nvram.is_supported():
        return default
    return nvram.get_value_or_default(key, default)


def _get_nvram_key_or_false(key):
    """Get

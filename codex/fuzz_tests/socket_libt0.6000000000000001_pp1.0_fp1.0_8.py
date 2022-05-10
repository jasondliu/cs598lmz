import socket
import sys

from . import constants, util

if sys.version_info >= (3, 0):
    from urllib.parse import unquote
else:
    from urllib import unquote

log = logging.getLogger(__name__)

#: Bytes that cannot be in a variable name
INVALID_VARIABLE_BYTES = set(
    b'\x00' +
    bytes(range(32)) +
    b'\x7f' +
    bytes(range(128, 256))
)

#: Bytes that cannot be in a variable value
INVALID_VALUE_BYTES = set(
    b'\x00\x01\x02\x03\x04\x05\x06\x07\x08'
    b'\x09\x0a\x0b\x0c\x0d\x0e\x0f'
    b'\x10\x11\x12\x13\x14\x15\x16\x17'
    b'\

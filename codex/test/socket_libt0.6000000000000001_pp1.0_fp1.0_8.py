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

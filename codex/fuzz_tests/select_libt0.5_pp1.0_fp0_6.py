import select
import socket
import sys

from . import __version__, logger
from . import utils
from . import client
from . import server
from . import tls

from .utils import (
    DEFAULT_PORT,
    DEFAULT_CIPHERS,
    DEFAULT_CERT_FILE,
    DEFAULT_KEY_FILE,
    DEFAULT_CA_FILE,
    DEFAULT_PID_FILE,
    DEFAULT_LOG_FILE,
    DEFAULT_LOG_LEVEL,
    DEFAULT_LOG_FORMAT,
    DEFAULT_LOG_DATE_FORMAT,
    DEFAULT_CONNECT_TIMEOUT,
    DEFAULT_IDLE_TIMEOUT,
    DEFAULT_MAX_BUFFER_SIZE,
    DEFAULT_MAX_CONNECTIONS,
)

DEFAULT_CONFIG = {
    'port': DEFAULT_PORT,
    'ciphers': DEFAULT_CIPHERS,
    'cert_file': DEFAULT_CERT_FILE,
    'key_file': DEFAULT_KEY_FILE,
    '

import select
import socket
import sys
import threading
import time
import traceback

from . import constants, exceptions, util
from .util import get_logger, get_logging_level, set_logging_level

logger = get_logger(__name__)

#: The default port for the Minecraft server.
DEFAULT_PORT = 25565

#: The default host for the Minecraft server.
DEFAULT_HOST = "localhost"

#: The default timeout for the Minecraft server.
DEFAULT_TIMEOUT = 5.0

#: The default encoding for the Minecraft server.
DEFAULT_ENCODING = "utf-8"

#: The default number of bytes for the Minecraft server.
DEFAULT_BUFFER_SIZE = 4096

#: The default number of bytes for the Minecraft server.
DEFAULT_MAX_QUEUE_SIZE = 100

#: The default number of bytes for the Minecraft server.
DEFAULT_RECONNECT_DELAY = 5.0

#: The default number of bytes for the Minecraft server.
DEFAULT_RECONNECT_

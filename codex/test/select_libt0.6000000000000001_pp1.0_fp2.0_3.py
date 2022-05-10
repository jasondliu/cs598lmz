import select
import socket
import ssl
import sys
import threading
import time
import traceback

from concurrent import futures

from . import compat
from . import config
from . import crypto
from . import events
from . import exceptions
from . import http
from . import log
from . import protocol
from . import util
from . import websocket

__all__ = ["Client", "connect"]

logger = log.get_logger(__name__)


class Client:
    """
    A Client is a WebSocket connection to a URL.
    """

import socket
import sys
import threading
import time
import traceback

from . import common
from . import config
from . import constants
from . import errors
from . import events
from . import logger
from . import utils
from . import version
from . import websocket
from .enums import Status
from .gateway import *
from .http import HTTPClient
from .state import ConnectionState
from .voice_client import VoiceClient
from .voice_websocket import VoiceWebSocket

log = logger.get_logger(__name__)


class Client(events.EventEmitter):
    """Represents a client connection that connects to Discord.

    This class is used to interact with the Discord WebSocket and API.

    A number of options can be passed to the :class:`Client`.

    Parameters
    -----------
    max_messages: Optional[:class:`int`]
        The maximum number of messages to store in the internal message cache.
        If the message cache in the :class:`Client` fills up then it could
        cause the client to disconnect from Discord.
    loop: Optional

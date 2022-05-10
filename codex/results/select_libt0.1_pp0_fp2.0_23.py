import select
import socket
import sys
import threading
import time
import traceback

from . import constants
from . import errors
from . import events
from . import utils
from . import version
from .client import Client
from .enums import Status
from .gateway import *
from .http import HTTPClient
from .state import ConnectionState
from .voice_client import VoiceClient
from .voice_ws import VoiceWebSocket

log = logging.getLogger(__name__)


class DiscordWebSocket(object):
    """Represents a websocket connection to Discord.

    This class is used to communicate with the Discord WebSocket gateway.

    Attributes
    -----------
    gateway: :class:`Gateway`
        The gateway connection.
    client: :class:`Client`
        The client that this websocket is bound to.
    """

    def __init__(self, client):
        self.client = client
        self.gateway = None
        self.http = HTTPClient(client)
        self.voice_clients = {}
        self.voice_connect_lock = asyncio

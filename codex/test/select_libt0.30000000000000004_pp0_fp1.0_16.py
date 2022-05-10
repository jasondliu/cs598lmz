import select
import socket
import sys
import time
import traceback

from . import constants
from . import errors
from . import events
from . import logger
from . import utils
from . import websocket
from .gateway import DiscordGateway
from .state import ConnectionState

log = logger.get_logger(__name__)


class DiscordWebSocket(websocket.WebSocketClient):
    def __init__(self, *, loop, gateway, **kwargs):
        super().__init__(**kwargs)

        self.loop = loop
        self.gateway = gateway
        self.state = ConnectionState(dispatch=self.gateway.dispatch, loop=self.loop)

        self.shard_id = gateway.shard_id
        self.shard_count = gateway.shard_count

        self.heartbeat_task = None
        self.heartbeat_timeout_task = None

        self.identify_task = None
        self.resume_task = None

        self.sequence = 0
        self.last_heartbeat = 0

       

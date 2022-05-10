import select
import socket
import sys
import threading
import time
import traceback

from . import constants
from . import errors
from . import events
from . import logger
from . import utils
from . import version
from .client import Client
from .enums import Status
from .gateway import Gateway
from .http import HTTPClient
from .state import ConnectionState
from .voice_client import VoiceClient

log = logger.get_logger(__name__)


class ClientUser(Client):
    """Represents the connected client.

    This is the user that is associated with the connected client.

    Attributes
    -----------
    id: :class:`int`
        The ID that discord uses to refer to the client.
    name: :class:`str`
        The name of the client.
    discriminator: :class:`str`
        The discriminator of the client.
    bot: :class:`bool`
        Whether the client is a bot or not.
    avatar: Optional[:class:`str`]
        The avatar hash of the client.
    """

    def

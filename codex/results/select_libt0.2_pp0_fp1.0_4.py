import select
import socket
import sys
import threading
import time
import traceback

from . import _common
from . import _constants
from . import _errors
from . import _events
from . import _util
from . import _websocket

__all__ = ['Client']


class Client:
    """
    A client for Discord.

    This class is used to interact with the Discord WebSocket and API.

    A number of options can be passed to the :class:`Client`.

    Parameters
    -----------
    max_messages: Optional[:class:`int`]
        The maximum number of messages to store in the internal message cache.
        The default is 5000.
    chunk_guilds_at_startup: Optional[:class:`bool`]
        Whether to request all guilds the client belongs to at startup.
        The default is :obj:`False`.
    fetch_offline_members: Optional[:class:`bool`]
        Whether to request offline members for every guild the
        client belongs to. This could be potentially expensive for large guilds.
        The

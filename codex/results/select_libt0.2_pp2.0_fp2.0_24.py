import select
import socket
import sys
import threading
import time
import traceback
import uuid

from . import __version__
from . import constants
from . import errors
from . import event
from . import message
from . import protocol
from . import util
from . import websocket

log = logging.getLogger(__name__)


class Client(object):
    """
    A client for the Slack Web API and Real Time Messaging protocol.

    :param token: Your API token.
    :param connect: Whether to connect to the Slack RTM API on instantiation.
    :param timeout: The number of seconds to wait for a reply from the server
                    before timing out.
    :param loop: An asyncio event loop to use for long-running connections.
    :param ssl: An SSLContext to use for the underlying websocket connection.
    :param proxy: A proxy URL to use for the underlying websocket connection.
    :param run_async: Whether to run the event loop in a background thread.
    :param kwargs: Additional keyword arguments to pass to the websocket
                   connection.

import select
import socket
import sys
import threading
import time

from . import constants
from . import exceptions
from . import utils
from . import version

__all__ = ['Client']

logger = logging.getLogger(__name__)


class Client(object):
    """
    A client for the MQTT v3.1.1 protocol.

    This class implements threaded interfaces to the network loop.  This
    allows you to have a background thread running the network loop, and then
    call publish() and subscribe() from your main thread.  This also allows
    you to integrate publish() and subscribe() calls into other event loops
    running in your main thread.

    The threaded interface uses a background thread to handle network events.
    This thread calls the on_message() callback when a message is received,
    and the on_disconnect() callback when the client disconnects.  It also
    handles timeouts and retries for QoS 1 messages.

    The threaded interface also provides a way to call a function periodically
    from the network loop thread.  This can be used to implement a keepalive
   

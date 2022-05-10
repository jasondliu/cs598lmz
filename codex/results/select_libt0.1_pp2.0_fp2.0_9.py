import select
import socket
import sys
import threading
import time
import traceback

from . import common
from . import config
from . import constants
from . import errors
from . import log
from . import messages
from . import protocol
from . import utils
from . import version

# pylint: disable=too-many-lines

# pylint: disable=too-many-instance-attributes
class Client(object):
    """
    A client for the MQTT protocol.

    This is the main class for the MQTT client. It provides methods for
    connecting to a broker, publishing messages, subscribing to topics and
    receiving published messages. It also provides methods for disconnecting
    cleanly.

    The client can be used in a synchronous or asynchronous way. In the
    synchronous way, the client blocks on some methods until they have
    completed. In the asynchronous way, the client uses callbacks to notify
    the application when a method has completed.

    The client can be used in a threaded or non-threaded way. In the threaded
    way, the client creates a thread to handle asynchronous

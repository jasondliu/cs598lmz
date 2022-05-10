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
from . import utils
from . import version

# pylint: disable=too-many-lines

# pylint: disable=too-many-instance-attributes
class Client(object):
    """
    Client class for interacting with a server.
    """

    def __init__(self, host, port, username, password,
                 client_id=None,
                 clean_session=True,
                 userdata=None,
                 protocol=mqtt.MQTTv311,
                 transport="tcp"):
        """
        Create a new instance of the client class.

        host: The hostname or IP address of the remote broker.
        port: The network port of the server host to connect to. Defaults to
            1883.
        client_id: The client ID for this client. If `None`, a random ID will
            be generated. If `clean_

import socket
import sys
import threading
import time
import traceback

import numpy as np

from . import constants
from . import exceptions
from . import utils
from . import version
from . import vrep
from . import vrep_objects

logger = logging.getLogger(__name__)


class VRepConnection(object):
    """
    V-REP connection.

    This class is used to connect to V-REP, and to retrieve and set data from
    V-REP.

    :param host: Hostname or IP address of the V-REP server.
    :param port: Port of the V-REP server.
    :param do_not_reconnect: If True, do not try to reconnect to V-REP when
        the connection is lost.
    :param sync_mode: If True, the connection will be synchronous.
    :param wait_for_trigger: If True, the connection will wait for a trigger
        from V-REP.
    :param time_out: Timeout in seconds.
    :param time_out_thread: Timeout in seconds for the thread

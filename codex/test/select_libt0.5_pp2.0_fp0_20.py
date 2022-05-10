import select
import socket
import sys
import time
import traceback
import uuid

from . import common
from . import config
from . import console
from . import daemon
from . import event
from . import log
from . import master
from . import net
from . import process
from . import protocol
from . import server
from . import ssh
from . import util

#-------------------------------------------------------------------------------

class Client(object):
    """
    Client object.  Handles all client-side operations.
    """

    #---------------------------------------------------------------------------
    # Client state constants.

    STATE_INITIALIZING = 0
    STATE_CONNECTING   = 1
    STATE_CONNECTED    = 2
    STATE_SHUTTING_DOWN = 3
    STATE_TERMINATED   = 4

    #---------------------------------------------------------------------------
    # Client event types.

    EVENT_INITIALIZED  = 0
    EVENT_CONNECTED    = 1
    EVENT_DISCONNECTED = 2
    EVENT_SHUTDOWN     = 3
    EVENT_TERMINATED   = 4

    #---------------------------------------------------------------------------


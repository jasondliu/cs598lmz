import select
import socket
import sys
import time
import threading
import traceback

from . import common
from . import key
from . import log
from . import message
from . import util

__all__ = ['Connection', 'Listener']

# Connection states:
#   'new': just created
#   'connecting': trying to connect to remote host
#   'connected': connected to remote host
#   'handshaking': performing handshake
#   'established': handshake complete
#   'closing': closing connection
#   'closed': connection closed

# Connection events:
#   'connect': connection established
#   'disconnect': connection closed
#   'error': error occurred

# Listener states:
#   'new': just created
#   'starting': starting listener
#   'listening': listening for connections
#   'stopping': stopping listener
#   'stopped': listener stopped

# Listener events:
#   'start': listener started
#   'stop': listener stopped
#   'error': error occurred
#   'connection': new connection received

# Connection and List

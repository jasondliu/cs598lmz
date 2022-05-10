import ctypes
import ctypes.util
import threading
import sqlite3
import time

import logging
logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)

# TODO:
#   * Add a "pending" state for messages that have been sent but not yet
#     acknowledged by the server.
#   * Add a "failed" state for messages that have been sent and not
#     acknowledged by the server.
#   * Add a "draft" state for messages that have not yet been sent.
#   * Add a "sending" state for messages that are being sent.
#   * Add a "sent" state for messages that have been sent and acknowledged
#     by the server.
#   * Add a "received" state for messages that have been received.
#   * Add a "read" state for messages that have been read.
#   * Add a "deleted" state for messages that have been deleted.

class Message(object):
    """
    A message.
    """

    def __init__(self, id, sender, recipient, timestamp, body, state):
        """
        Initialize a

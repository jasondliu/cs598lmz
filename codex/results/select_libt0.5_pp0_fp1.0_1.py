import select
import threading

from datetime import datetime
from time import sleep

from . import config
from . import utils
from . import consts


def send_message(sock, message):
    """
    Send a message to the server.
    """
    # Prefix each message with a 4-byte length (network byte order)
    message = utils.encode(message)
    message = struct.pack('>I', len(message)) + message
    sock.sendall(message)


def recv_message(sock):
    """
    Read messages from the server.
    """
    # Read message length and unpack it into an integer
    raw_msglen = recvall(sock, 4)
    if not raw_msglen:
        return None
    msglen = struct.unpack('>I', raw_msglen)[0]
    # Read the message data
    return recvall(sock, msglen)


def recvall(sock, n):
    """
    Helper function to recv n bytes

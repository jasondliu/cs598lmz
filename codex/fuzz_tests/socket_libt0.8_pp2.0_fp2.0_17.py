import socket
import threading
from binascii import hexlify
from datetime import datetime
from struct import pack, unpack
from time import sleep
from io import BytesIO

from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA256
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Cipher import AES

import asn1parser
import certparser
import tlsparser
import tlsdatabase

from tlsdatabase import *

from . import const
from . import logger


def recvall(socket, length):
    """Read the given amount of bytes from the socket.
    Will block until all bytes are received, or
    raise an exception.

    Args:
        socket (socket): The socket to receive bytes from.
        length (int): Amount of bytes to receive.

    Returns:
        bytes: The received data.
    """
    data = bytes()
    while len(data) < length:
        tmp = socket.recv(length - len(data))
        if

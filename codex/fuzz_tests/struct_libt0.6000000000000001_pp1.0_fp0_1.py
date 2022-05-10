import _struct
from binascii import hexlify
from time import time
from random import randint, choice
from hashlib import sha1
from string import ascii_letters, digits
from .utils import get_random_bytes, get_random_string
from .exceptions import (
    NotEnoughData,
    InvalidPacket,
    EncryptionError,
    DecryptionError,
    AuthenticationError
)


class Packet(object):
    """
    Base packet class.
    """

    HEADER_FORMAT = '!BB'
    HEADER_LENGTH = _struct.calcsize(HEADER_FORMAT)

    # Packet type
    TYPE_CONTROL = 0x00
    TYPE_DATA = 0x01

    # Control packet subtypes
    SUBTYPE_CONNECT = 0x00
    SUBTYPE_CONNACK = 0x01
    SUBTYPE_DISCONNECT = 0x02
    SUBTYPE_PINGREQ = 0x03
    SUBTYPE_PINGRESP = 0x04
    SUBTYPE_DATA = 0x05

    #

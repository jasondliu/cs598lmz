import socket
import random
import threading
from collections import namedtuple
from Crypto.Cipher import AES
from Crypto.Hash import SHA256

from .base import BaseNode, BaseProtocol
from ..common.constants import MESSAGE_CODE, MESSAGE_TYPE
from ..common.exceptions import NodeException, ProtocolException
from ..common.util import get_ip_address
from ..common.logging import log


class Node(BaseNode):
    PROTOCOL_CLASS = 'TCP'
    LISTEN_PORT = 8056
    MAX_CONNECTION = 8
    PORT_RANGE_START = 8056
    PORT_RANGE_END = 8076

    def __init__(self, node_id, secret, name, description, addr=None, port=None,
                 *args, **kwargs):
        super().__init__(node_id, secret, name, description, addr, port,
                         *args, **kwargs)

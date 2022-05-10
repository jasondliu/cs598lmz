import _struct
import logging
import socket
import time

from .common import (
    HOST,
    PORT,
    Version,
    build_hello,
    build_peer_announce,
    build_peer_info,
    build_ping,
    build_pong,
    build_verack,
)

logger = logging.getLogger(__name__)


class Connection(object):
    def __init__(self,
                 host=HOST,
                 port=PORT,
                 version=Version,
                 services=None,
                 nonce=None,
                 time=None,
                 start_height=None,
                 user_agent=None,
                 relay=None,
                 ):
        self.host = host
        self.port = port
        self.socket = None
        self.version = version
        self.services = services
        self.nonce = nonce
        self.time = time
        self.start_height = start_height
        self.user_agent = user_agent
        self.relay = relay

    def connect(

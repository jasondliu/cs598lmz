import socket
import select
import errno
import logging
import struct
import decimal

from connector.protocol import Protocol
from connector.utils import parse_config
from connector.exceptions import RPCError
from connector import models

protocol = Protocol()
logger = logging.getLogger(__name__)


class Daemon(object):
    """A class to encapsulate the RPCDaemon"""

    def __init__(self, chainparams=None, conf={}):
        """Make a new RPCDaemon instance with the given config"""
        self.conf = parse_config(conf)
        if not self.conf:
            raise RuntimeError("Could not find configuration")

        self.conf.update(
            self.conf.get(chainparams.lower(), {}) if chainparams else {})

        self.chainparams = chainparams

        self.protocol = protocol

        self.netid = 'mainnet'  # TODO
        self.errmap = {  # code to exception class mapping
            -1: RPCError,
        }

        self._sock = socket.socket

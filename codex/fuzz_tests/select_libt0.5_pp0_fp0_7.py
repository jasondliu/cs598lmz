import select
import socket
import sys
import time

from ndn import KeychainDigest
from ndn.encoding import Name, TlvModel, TlvWireFormat, Component
from ndn.encoding.tlv_model import Tlv
from ndn.types import InterestNack, InterestTimeout
from typing import List

from . import __version__
from . import config
from . import log
from . import utils


class Nfdc(object):
    """
    The NFD management client.
    """

    _LOG = log.get_logger("NFDC")

    def __init__(self, config: config.Config, nfd_host: str, nfd_port: int) -> None:
        """
        Initialize the Nfdc.

        :param config: configuration
        :param nfd_host: NFD host
        :param nfd_port: NFD port
        """
        self._config = config

        self._nfd_host = nfd_host
        self._nfd_port = nfd_port

        self._client_key = None


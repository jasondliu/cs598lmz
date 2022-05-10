import weakref
import asyncio
import logging

from .channel_factory import DatagramChannelFactory, MulticastDatagramChannelFactory
from .channel_connection import ChannelConnection
from .channel_event import ChannelEvent
from .channel import BaseChannel
from .ip_address import IPAddress
from .lb_socket_status import LBSocketStatus
from .broadcast_scope import BroadcastScope
from .channel_data_limit import ChannelDataLimit
from .crypto import Crypto
from .ip_endpoint import IPEndpoint

logger = logging.getLogger(__name__)


class UdpChannel(BaseChannel):
    def __init__(self, socket, address, identity=None, is_multicast=False, shared_key=None, is_ssl=False):
        super().__init__(socket, address, identity=identity, shared_key=shared_key, is_ssl=is_ssl)
        self.is_multicast = is_multicast

    def is_open(self):
        """
        Checks if channel is open.

        :return bool:
        """

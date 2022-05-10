import selectors

from datetime import datetime
from typing import Callable
from typing import IO
from typing import List
from typing import Optional
from typing import Tuple

from ipaddress import ip_address
from ipaddress import ip_network

from . import _stream
from . import _tcp
from . import constants
from . import exceptions
from . import family
from . import _events
from . import _events_impl
from . import _low_level_impls
from . import _selector_events
from . import _util
from .log import logger

__all__ = ('DatagramTransport', 'open_datagram_transport')


class DatagramTransport:
    """Datagram transport.

    A datagram transport represents a local endpoint of communication
    that supports datagram oriented socket operations.
    """

    def __init__(self, transport: _low_level_impls.DatagramTransport,
                 protocol: asyncio.DatagramProtocol,
                 loop: asyncio.AbstractEventLoop):
        self._transport = transport
        self._protocol = protocol
        self

import weakref

from typing import TYPE_CHECKING, Any, Dict, List, Optional, Union, cast

from .enums import ConnectionState, SocketState
from .decorators import require_connection, require_ready
from .errors import InvalidStateError, NotConnectedError
from .meta import MessageData
from .namespace import Namespace
from .packet import Packet, decode_packet
from .parser import Decoder, Encoder
from .utils import random_id, run_callback

if TYPE_CHECKING:
    from .client import Client
    from .handshake import HandshakeService
    from .namespace import NamespaceMetadata
    from .heartbeats import HeartbeatService

__all__ = ["Socket"]



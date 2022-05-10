import weakref

from . import base
from . import compat
from . import errors
from . import helpers
from . import protocol

from .log import logger
from .config import config
from .utils import is_valid_ip
from .utils import is_valid_port
from .utils import get_ip_from_host
from .utils import get_server_address
from .utils import to_bytes
from .utils import to_str
from .utils import parse_header
from .utils import parse_host
from .utils import parse_proxy


class Socks5Client(base.BaseObject):
    """
    Socks5 client implementation.

    :param str username: username
    :param str password: password
    :param int timeout: (optional) timeout for connection, in seconds

    :ivar str remote_address: remote ip address
    :ivar int remote_port: remote port number
    :ivar str rsv: reserved field
    :ivar str atyp: address type, 0x01 - ipv4, 0x03 - domain name, 0x04 - ipv6
    """
    __sl

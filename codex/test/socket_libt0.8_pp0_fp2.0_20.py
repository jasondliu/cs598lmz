import socket
import ipaddress
import ssl

from typing import Optional
from typing import List
from typing import Mapping
from typing import Tuple
from typing import TYPE_CHECKING

from .colors import green
from .colors import cyan
from .colors import red
from .colors import yellow
from .colors import purple
from .colors import magenta
from .colors import blue
from .colors import white
from .colors import bold
from .colors import clean
from .colors import underline
from .colors import grey

if TYPE_CHECKING:
    from typing import Set
    from typing import Any

sock_type_strs = {
    socket.SOCK_STREAM: 'TCP',
    socket.SOCK_DGRAM: 'UDP',
}


def colored(color: str, text: str) -> str:
    return color + text + clean


class Address:
    def __init__(self, family: int, address: str, port: Optional[int]=None):
        self.family = family

import _struct

from . import _constants
from . import _compat
import _base

__all__ = [ 'Connection', 'Packet', 'PacketError' ]

class Connection(_base.Connection):
    def __init__(self, wrapped):
        super(Connection, self).__init__(wrapped)
        self.bound = 0
        self.peer = None
        self.flags = 0
        self.tunnel = 0
        self.rflags = 0

    def bind(self, address = None):
        if self.bound:
            raise _compat.socket_error(errno.EINVAL, 'socket already bound')

        if address is None:
            address = ('', 0)
        else:
            address = _compat.inet_pton(address)

        if address[0] or address[1]:
            self.flags |= _constants.BPF_F_ADDR_FILTER

        self.bound = 1

        self.wrapped.bind(address)
        self.peer = address

    def setsockopt(self, *args,

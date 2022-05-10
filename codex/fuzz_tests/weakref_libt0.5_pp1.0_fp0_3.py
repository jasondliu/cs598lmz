import weakref

from .. import core
from .. import _base
from .. import _thread
from .. import _net
from .. import _core
from .. import _util
from .. import _compat

from . import _proactor_events

__all__ = ['BaseProactorEventLoop', 'BaseProactorEventLoopPolicy']


class BaseProactorEventLoop(_base.BaseEventLoop):
    """Base class for proactor event loops.

    This implements the event loop on top of a proactor.
    """

    def _socketpair(self):
        """socket.socketpair() replacement."""
        raise NotImplementedError

    @property
    def _ProactorSocketTransport(self):
        """Transport class for socket objects."""
        raise NotImplementedError

    @property
    def _ProactorFileTransport(self):
        """Transport class for file descriptors."""
        raise NotImplementedError

    def _make_socket_transport(self, sock, protocol, waiter=None,
                               extra=None, server=None):
        return self._Proactor

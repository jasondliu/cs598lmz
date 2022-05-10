import weakref

import trio
from trio import socket
from trio.abc import AsyncResource
from typing import Any, Callable, Collection, Deque, Optional, Sequence, Set
from typing_extensions import Protocol

from . import core
from .core import (
    _Address,
    _Transport,
    _TransportBase,
    Address,
    Transport,
    TransportClosed,
    _wait_read,
    _wait_write,
)

log = logging.getLogger(__name__)


class _DataQueueView:
    def __init__(self, data) -> None:
        self.data = data

    def __len__(self):
        return len(self.data)

    def __iter__(self):
        return iter(self.data)

    def __repr__(self):
        return repr(self.data)


class _MemoryTransportData:
    def __init__(self) -> None:
        self._send_queue: Deque[Any] = collections.deque()
        self._receive_queue: Deque[

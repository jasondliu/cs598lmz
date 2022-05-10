import select
import sys
import types

from . import _pyev

__all__ = ['Loop', 'default_loop', 'Flags', 'EVBACKEND']

EVBACKEND = _pyev.backend()

class Flags:
    NOINOTIFY = _pyev.EVFLAG_NOINOTIFY
    FORKCHECK = _pyev.EVFLAG_FORKCHECK
    SIGNALFD = _pyev.EVFLAG_SIGNALFD
    NOSIGMASK = _pyev.EVFLAG_NOSIGMASK
    BACKEND_MASK = _pyev.EVBACKEND_MASK
    RECEIPT = _pyev.EVFLAG_RECEIPT


class Loop:

    def __init__(self, flags=0):
        self._loop = _pyev.Loop(flags)
        self._loop.data = self
        self._events = {}

    def __del__(self):
        self.destroy()

    def destroy(self):
        if self._loop is not None:
            self._loop.destroy()
            self._loop

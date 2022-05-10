import weakref
import sys
import traceback
import types

import logging
logger = logging.getLogger(__name__)

from ... import utils
from ...utils import _log_warn_or_error, _log_error
from ... import exceptions

from . import base
from . import _sigslot
from . import _sigslot_impl
from . import _sigslot_impl_weakref

__all__ = ['Signal']

class Signal(base.Signal):
    __slots__ = ['_impl']

    def __init__(self, *args, **kwargs):
        self._impl = _sigslot_impl.SignalImpl(*args, **kwargs)

    def connect(self, slot, *args, **kwargs):
        return self._impl.connect(slot, *args, **kwargs)

    def disconnect(self, slot):
        return self._impl.disconnect(slot)

    def emit(self, *args, **kwargs):
        return self._impl.emit(*args, **kwargs)


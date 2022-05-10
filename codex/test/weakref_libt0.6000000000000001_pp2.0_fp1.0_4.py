import weakref
from contextlib import contextmanager

from . import log


#: A default logger for :class:`Progress` instances.
_logger = log.manager.getLogger(__name__)



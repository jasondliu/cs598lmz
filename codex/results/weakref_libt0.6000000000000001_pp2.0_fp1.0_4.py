import weakref
from contextlib import contextmanager

from . import log


#: A default logger for :class:`Progress` instances.
_logger = log.manager.getLogger(__name__)


class Progress(object):
    """
    A context manager for reporting progress on a task.

    :param setup: A callable to call when the context manager is entered.
        The callable should accept a single argument, the :class:`Progress`
        instance.
    :param update: A callable to call repeatedly while the context manager is
        active.  The callable should accept a single argument, the
        :class:`Progress` instance.
    :param logger: A logger to use for reporting progress.

    If the ``setup`` callable returns a value, the context manager will yield
    that value.

    If the ``update`` callable returns a value, the context manager will
    yield that value on each iteration.

    The ``setup`` and ``update`` callables may be :func:`str.format`-style
    format strings.

    The :class:`Progress` instance will call :

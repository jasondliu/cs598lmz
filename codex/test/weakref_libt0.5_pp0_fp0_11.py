import weakref

from . import (
    abc,
    errors,
    futures,
    protocols,
    tasks,
)

__all__ = [
    'AbstractEventLoop',
    'BaseEventLoop',
    'Handle',
    'TimerHandle',
    'get_event_loop',
    'new_event_loop',
    'set_event_loop',
]


class Handle(object):
    """Object returned by call_soon, call_later, call_at."""

    __slots__ = ('_callback', '_args', '_cancelled', '_loop')

    def __init__(self, callback, args, loop):
        if not callable(callback):
            raise TypeError('a callable object is required')
        self._callback = callback
        self._args = args
        self._cancelled = False
        self._loop = loop


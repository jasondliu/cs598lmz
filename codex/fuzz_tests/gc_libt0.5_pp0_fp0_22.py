import gc, weakref
from time import time
from threading import Thread, Lock

from . import errors
from . import utils

class Subscription(object):
    '''Subscription object for :class:`Session`.

    This object is created by :class:`Session` and is used to
    subscribe to a specific topic.

    You can then use :meth:`wait` to wait for the first message,
    and :meth:`pop` to retrieve the messages and remove them from
    the internal buffer.

    You can also use :meth:`get` to get the messages without
    removing them from the internal buffer.

    .. note::

        You can only use one of :meth:`wait`, :meth:`pop` or
        :meth:`get` at a time.

    .. warning::

        If you do not use one of the above methods, you *must*
        use :meth:`unsubscribe` to clear the subscription,
        otherwise you will leak memory.

    .. warning::

        If you do use one of the above methods, you *must*
        use

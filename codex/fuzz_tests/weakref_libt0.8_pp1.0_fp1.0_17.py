import weakref

from . import BaseSpecial, NoNodes
from .exceptions import BlockSyntaxError


__all__ = ('Value', 'filter_or_reject', 'filter', 'reject')


class Value(BaseSpecial):
    """
    :class:`Value` is a simple block that just outputs its contents, in the
    order in which those contents are given in the block header.

    In order to simplify the creation of filters, :class:`Value` objects are
    callable, and can be called with a stream to filter. The callable syntax
    has the advantage of being easier to read, and also allows :class:`Value`
    objects to be used with (some of) the standard Python filter functions,
    such as :func:`filter` and :func:`reject` in order to filter a stream.

    Example::

        >>> value = Value(test, 'first', 'second', 'third')
        >>> list(value(('first', 'second', 'third')))
        ['first', 'second', 'third']
        >>> list(value(('second', 'third', 'fourth

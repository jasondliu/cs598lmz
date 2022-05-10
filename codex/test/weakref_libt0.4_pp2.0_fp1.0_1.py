import weakref

from . import _base
from . import _signals
from . import _utils


class _BaseSignal(object):
    """
    Base class for all signals.
    """

    def __init__(self, name, doc=None):
        self.name = name
        self.__doc__ = doc

    def __str__(self):
        return self.name

    def __repr__(self):
        return '<%s %s>' % (self.__class__.__name__, self.name)

    def __eq__(self, other):
        return (
            isinstance(other, self.__class__) and
            self.name == other.name
        )

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash(self.name)

    def __call__(self, *args, **kwargs):
        return self.emit(*args, **kwargs)


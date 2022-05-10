import weakref

from six import add_metaclass

from . import _base
from . import _impl


@add_metaclass(_base.Meta)
class _WeakKeyDictionary(_base._Dictionary):
    """A weak key dictionary implementation."""

    def __init__(self, *args, **kwargs):
        super(_WeakKeyDictionary, self).__init__(*args, **kwargs)
        self._dict = weakref.WeakKeyDictionary(*args, **kwargs)

    def __repr__(self):
        return '{0}({1})'.format(
            self.__class__.__name__,
            repr(self._dict)
        )

    def __str__(self):
        return str(self._dict)

    def __iter__(self):
        return iter(self._dict)

    def __len__(self):
        return len(self._dict)

    def __contains__(self, key):
        return key in self._dict


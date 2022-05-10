import weakref

from . import base
from . import _util as util

class _Base(base._Base):
    _attribute_names = ('name', 'value', 'index', 'type')
    _attribute_names_with_defaults = ('index', 'type')

    def _init(self, name, value):
        self.name = name
        self.value = value
        self.index = None
        self.type = None

    def _equal(self, other):
        return (self.name == other.name and
                self.value == other.value and
                self.index == other.index and
                self.type == other.type)

    def _notequal(self, other):
        return not self._equal(other)

    def _hash(self):
        return hash(self.name)

    def _repr(self):
        return 'Parameter(%r, %r)' % (self.name, self.value)

    def _str(self):
        return '%s=%s' % (self.name, self.value)

    def _get

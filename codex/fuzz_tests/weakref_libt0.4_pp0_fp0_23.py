import weakref

import numpy as np

from . import _utils

# TODO:
# - add support for more than one axis
# - add support for more than one dimension
# - add support for more than one data type
# - add support for attributes
# - add support for groups

class _Base(object):
    """Base class for all objects in the hierarchy."""
    def __init__(self, parent, name):
        self._parent = weakref.ref(parent)
        self._name = name

    @property
    def parent(self):
        return self._parent()

    @property
    def name(self):
        return self._name

    @property
    def path(self):
        if self.parent is None:
            return self.name
        else:
            return self.parent.path + '/' + self.name

    def __repr__(self):
        return '<{} "{}">'.format(self.__class__.__name__, self.path)


class _Group(_Base):
    """Group object."""
    def __

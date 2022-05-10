import gc, weakref
from collections import OrderedDict

from .base import Base
from . import utils
from . import _compat
from . import _compat_collections

class _Fields(object):
    """
    This class is used to store the fields of a model. It is a dictionary
    with some additional methods.
    """
    def __init__(self, fields):
        self.fields = fields

    def __getitem__(self, name):
        return self.fields[name]

    def __setitem__(self, name, value):
        self.fields[name] = value

    def __delitem__(self, name):
        del self.fields[name]

    def __iter__(self):
        return iter(self.fields)

    def __len__(self):
        return len(self.fields)

    def __contains__(self, name):
        return name in self.fields

    def __eq__(self, other):
        return self.fields == other

    def __ne__(self, other):
        return self.fields !=

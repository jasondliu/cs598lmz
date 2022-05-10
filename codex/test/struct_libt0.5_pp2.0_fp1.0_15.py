import _struct

from . import _bintools
from . import _exceptions
from . import _util

class _Struct(object):
    def __init__(self, struct_type, values):
        self.struct_type = struct_type
        self.values = values

    def __repr__(self):
        return '<%s %s>' % (self.struct_type, self.values)

    def __getitem__(self, key):
        return self.values[key]

    def __setitem__(self, key, value):
        self.values[key] = value

    def __len__(self):
        return len(self.values)

    def __getattr__(self, name):
        return self.values[name]

    def __setattr__(self, name, value):
        if name in ('struct_type', 'values'):
            super(_Struct, self).__setattr__(name, value)
        else:
            self.values[name] = value



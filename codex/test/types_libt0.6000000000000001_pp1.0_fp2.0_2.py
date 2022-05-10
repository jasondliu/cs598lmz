import types
types.ModuleType.__doc__ = ""

import sys

class Module(types.ModuleType):
    __doc__ = ""
    def __getattribute__(self, name):
        if name.startswith('_'):
            return types.ModuleType.__getattribute__(self, name)
        if name not in sys.modules:
            import_module(name)
        return sys.modules[name]
    def __setattr__(self, name, value):
        raise AttributeError("You cannot set attributes of the %s module" % __name__)
    def __delattr__(self, name):
        raise AttributeError("You cannot delete attributes of the %s module" % __name__)

# This is the actual module object to be used by "import *".
sys.modules[__name__] = Module(__name__)

# Now we can import the rest of the modules.
from . import _importhooks
from . import _io
from . import _warnings
from . import abc
from . import ast
from . import asynchat

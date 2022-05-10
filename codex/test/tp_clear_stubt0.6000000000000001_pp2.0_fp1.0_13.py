import gc, weakref

class LateFin:
    __slots__ = ('ref',)
    def __del__(self):
        global func
        func = self.ref()

class Cyclic(tuple):
    __slots__ = ()
    def __del__(self):
        self[1].ref = weakref.ref(self[0])
        global latefin
        del latefin

latefin = LateFin()
func = lambda: None
cyc = tuple.__new__(Cyclic, (func, latefin))

func.__module__ = cyc
del func, cyc

gc.collect()

import sys
if sys.version_info[:2] == (2, 4):
    # Work around a bug in Python 2.4, which doesn't clear the module
    # properly in this case.
    sys.modules.pop('test_weakref', None)

# If we have a reference cycle involving a module, the module
# will be part of a reference cycle with the module's dictionary,
# which will be part of a reference cycle with the module's
# weakrefs list, which will be part of a reference cycle with
# the module.

# This is a regression test for SF bug #672440.

import sys
import weakref

class Module(types.ModuleType):
    def __init__(self, name):
        types.ModuleType.__init__(self, name)
        self.__dict__['cycle'] = self

m = Module("test_weakref")

# Create a reference *to* the module, but not *from* the module,
# so that m is the only reference to the module.
r = weak

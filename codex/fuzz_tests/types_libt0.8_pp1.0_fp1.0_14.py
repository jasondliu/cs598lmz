import types
types.ModuleType.__repr__ = lambda m: m.__name__

abc = sys.modules['_py_abc']
sys.modules['abc'] = abc
sys.modules['_py_abc'] = None

# Prepare builtins module.
import _io
import _thread
import _locale
import _imp
import _stat
import _random
import _elementtree
import _pickle
import errno

import marshal
import posix
import posixpath
import zipimport

builtins_module = types.ModuleType("builtins")
sys.modules['builtins'] = builtins_module
for name in dir(_io):
    builtins_module.__dict__[name] = getattr(_io, name)
for name in dir(_thread):
    builtins_module.__dict__[name] = getattr(_thread, name)
for name in dir(_locale):
    builtins_module.__dict__[name] = getattr(_locale, name)
for name in dir(_imp):
    builtins_module.__dict__[name] =

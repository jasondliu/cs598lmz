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

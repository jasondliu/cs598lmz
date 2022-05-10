import types
types.ModuleType

import sys
sys.modules.keys

# reloading modules
import hello
import imp
imp.reload(hello)

# import *
from hello import *
import hello
from hello import hello
hello

# __import__
__import__('hello')

# importlib
import importlib
importlib.import_module('hello')

# importlib.reload
importlib.reload(hello)

# importlib.find_loader
importlib.find_loader('hello')
importlib.find_loader('os')

# importlib.util.find_spec
importlib.util.find_spec('hello')
importlib.util.find_spec('os')

# importlib.util.find_spec(name, path=None)
importlib.util.find_spec('hello', path=['/tmp'])

# importlib.util.find_spec(name, path=None)
importlib.util.find_spec('hello', path=['/tmp'])

# importlib.util.find_spec(name, path=

from types import FunctionType
list(FunctionType(l.__code__, globals(), "").__globals__.keys())

from sys import modules, path

modules

from inspect import getmembers, ismodule
import base64
list(map(lambda x: (x, base64.b64encode(x.encode()).decode()), 
         filter(lambda x: not ismodule(modules[x]),
                filter(lambda x: not x.startswith("_"),
                       list(modules.keys())))))

from importlib import import_module

import_module("pandas")

from types import FunctionType

# FunctionType(code, globals, defaults, closure)
# - code is a code object, created by compile() or by the exec statement.
# - globals must be a dictionary.
# - defaults can be None or a tuple containing default argument values.
# - closure can be None or a tuple of cells that contain bindings for the function’s free variables.

from sys import modules
FunctionType(modules["pandas"].DataFrame.__init__.__code__, globals(),

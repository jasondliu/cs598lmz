import _struct
import _string
import _random
import _re
import math
import operator as op
import sys
import time
import __builtin__

from types import ModuleType, FunctionType

# Hack to support non-ascii code points in python2.7
if sys.version_info[0] == 2:
    reload(sys)
    sys.setdefaultencoding('utf-8')

# Expose all standard library modules.
__all__ = [name for name in sys.builtin_module_names
           if name not in ('__main__', '__builtin__', 'builtins')]

# Use the same module object as the standard module of the same name.
for name in __all__:
    module = sys.modules[name] = ModuleType(name)
    module.__file__ = "<stdlib>"
    module.__package__ = name
    module.__loader__ = None

    # Give standard library modules __path__ attributes.
    if name in ('array', 'collections', 'collections.abc', 'functools',
                'heapq',

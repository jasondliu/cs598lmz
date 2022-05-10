import types
types.ModuleType.__dict__.__setitem__('__getattr__', lambda self, name: self.__getattribute__(name))
types.ModuleType.__dict__.__setitem__('__setattr__', lambda self, name, value: self.__setattr__(name, value))
types.ModuleType.__dict__.__setitem__('__delattr__', lambda self, name: self.__delattr__(name))

# This is a hack to make the module work with both Python 2 and 3
# The aim is to have a single codebase
try:
    import __builtin__ as builtins # Python 2
except ImportError:
    import builtins # Python 3

# This is a hack to make the module work with both Python 2 and 3
# The aim is to have a single codebase
try:
    import __builtin__ as builtins # Python 2
except ImportError:
    import builtins # Python 3

# This is a hack to make the module work with both Python 2 and 3
# The aim is to have a single codebase
try:
    import __

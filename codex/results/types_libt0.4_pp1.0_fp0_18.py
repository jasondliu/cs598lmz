import types
types.ModuleType.__dict__.__setitem__('__getattr__', lambda self, name: self.__getattribute__(name))
types.ModuleType.__dict__.__setitem__('__setattr__', lambda self, name, value: self.__setattr__(name, value))
types.ModuleType.__dict__.__setitem__('__delattr__', lambda self, name: self.__delattr__(name))

# this is a hack to make sure that the module is loaded
# before we try to set the attributes
import sys
import types

# this is a hack to make sure that the module is loaded
# before we try to set the attributes
import sys
import types

# this is a hack to make sure that the module is loaded
# before we try to set the attributes
import sys
import types

# this is a hack to make sure that the module is loaded
# before we try to set the attributes
import sys
import types

# this is a hack to make sure that the module is loaded
# before we try to set the attributes
import sys
import types



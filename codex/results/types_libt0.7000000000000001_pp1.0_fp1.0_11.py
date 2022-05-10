import types
types.ModuleType('test')

# Changing a module name
import sys
sys.modules['test'] = sys.modules['types']
print test.ModuleType

# Reloading modules
import types
reload(types)
types.ModuleType('test')

# Using sys.path to find modules
import sys
sys.path.append('/home/craig/diveintopython3/examples/')
import mymodule
mymodule.title

# Using __name__
import mymodule
mymodule.__name__
mymodule.title

# Importing from a package
import diveintopython3.examples.mymodule
diveintopython3.examples.mymodule.title

# Importing * from a package
from diveintopython3 import examples
examples.mymodule.title

# Importing * from a module
from examples.mymodule import *
title

# Naming conflicts
from diveintopython3 import *
examples.zipfile_example.title
diveintopython3.http.client.HTTPConnection

# Using __all__

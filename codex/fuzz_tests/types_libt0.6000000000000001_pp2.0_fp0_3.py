import types
types.ModuleType('scipy').__file__

# If a module is not found, the above line gives an error. 
# You can then copy the path and add it to the sys.path list as follows:

import sys
sys.path.append('/Users/myname/Desktop/my_module_directory')

# The path can be absolute or relative. 
# If it is relative, you need to make sure to provide the full path. 
# You can also use the os.path module to help you find the exact path to the desired directory.

# If you want to import your module from a different directory, 
# you can use the following syntax:

from directory_name import module_name

# If you would like to use the contents of the module without having to prefix the name of the module, 
# you can use the following syntax:

from directory_name.module_name import *

# This will import all of the contents of the module into your current namespace. 
# This is generally not recommended, as it can lead to namespace pollution. 
# It is better to import specific functions and classes

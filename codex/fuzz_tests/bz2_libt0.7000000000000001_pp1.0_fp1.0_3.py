import bz2
bz2.compress

# importing modules from a subpackage
from package import subpackage
subpackage.module_y.Spam

# from ... import *
from package import *
module_x
module_y

# from ... import * can be used to import subpackages as well
from package.subpackage import *
module_y

# Relative imports
from . import module_x
module_x

# Explicit relative imports
from .module_x import *
Spam

# Relative imports can go up the tree
from .. import module_y
module_y

# Relative imports can go up the tree and then back down
from ..subpackage import module_y
module_y

# Explicit relative imports
from ..subpackage.module_y import Spam
Spam

import ctypes
ctypes.cast(0, ctypes.py_object)

#
# The following is a hack to keep the interpreter from exiting when
# Ctrl-C is pressed.
#
import atexit
def nothing():
    pass
atexit.register(nothing)

#
# Import the low-level C++ module.
#
from _pydrake import *

#
# Import the Python modules.
#
from pydrake.autodiffutils import *
from pydrake.common import *
from pydrake.common.cpp_param import *
from pydrake.common.eigen_geometry import *
from pydrake.common.find_resource import *
from pydrake.common.test_utilities import *
from pydrake.common.value import *
from pydrake.geometry import *
from pydrake.lcm import *
from pydrake.multibody import *
from pydrake.multibody.parsing import *
from pydrake.multibody.plant import *
from pydrake.multibody.tree import *
from pydrake

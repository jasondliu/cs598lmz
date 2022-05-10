import types
types.ModuleType.__repr__ = lambda self: '<module %s>' % self.__name__

#-----------------------------------------------------------------------------
# Imports
#-----------------------------------------------------------------------------

# Standard library imports
import os
import sys
import warnings

# Our own imports
from IPython.core import release
from IPython.core.error import TryNext
from IPython.core.extensions import ExtensionManager
from IPython.core.profiledir import ProfileDir
from IPython.utils.path import get_ipython_dir, get_ipython_package_dir
from IPython.utils.process import find_cmd, pycmd2argv
from IPython.utils.traitlets import (
    Bool, CBool, CaselessStrEnum, Dict, Enum, Float, Integer, List, Unicode,
)
from IPython.utils.warn import error, warn

#-----------------------------------------------------------------------------
# Globals and constants
#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------
# Local utilities
#-----------------------------------------------------------------------------

def get_pasted_lines(sentinel, raw=False, encoding=None):
    """Get lines pasted from

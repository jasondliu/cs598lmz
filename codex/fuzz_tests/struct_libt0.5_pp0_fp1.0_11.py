import _struct
import _time
import _thread
import _threading
import _traceback
import _types
import _warnings
import _weakref
import _weakrefset
import _winreg
import _xxsubinterpreters


# Re-export all built-in module names from the _bootlocale module.
# This is the only module that is implemented in C.
from _bootlocale import *

# The builtins module is special.  It has no pre-defined name and
# is never explicitly imported.
import __builtin__

# Set sys.path and sys.prefix
import sys
sys.path = sys.prefix = None

# Set up the import machinery
import imp
import _imp

# Set up sys.argv.
import os
argv0 = os.path.abspath(sys.executable)
sys.argv = [argv0]

# Set up sys.path_importer_cache
import _frozen_importlib
_frozen_importlib.install()

# Set up _frozen_importlib.BuiltinImporter
import _

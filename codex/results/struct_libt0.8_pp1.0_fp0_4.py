import _struct
import _subprocess
import _symtable
import _thread
import _threading_local
import _time
import _codecs
import _weakref
import _weakrefset
import _sitebuiltins

# Extensions are dynamically loaded when first imported.
_sysconfigdata = None
_testimportpreload = False

# Preload the bootstrap modules.
_frozen_importlib = _imp.init_frozen("_frozen_importlib")
_imp.init_frozen("_frozen_importlib_external")
_bootstrap = _imp.create_builtin("_bootstrap")
_bootstrap_external = _imp.create_builtin("_bootstrap_external")
del _frozen_importlib

# Initialize internal modules.
_imp.init_frozen("_warnings")

_shutdown = False

def _set_module(modulename, module):
    """Set the module object in the sys.modules dict.

    This should be used by importers to set the module object in
    sys.modules.

    This function is needed because

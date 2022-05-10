import lzma
lzma.decompress(b"")

import defusedxml.ElementTree
_ = defusedxml.ElementTree
import defusedxml.minidom
_ = defusedxml.minidom

# The following modules are only available on Windows.
if sys.platform == "win32":
    import winreg


def _import_module(name):
    """Import a module and return the module object."""
    __import__(name)
    return sys.modules[name]


def _import_module_with_name(name, modname):
    """Import a module as a different name and return the module object.

    This is used to import the same module under different names to create
    new reference cycles and simulate a more realistic application.
    """
    import importlib
    importlib.import_module(name)
    return sys.modules[modname]


def _load_module(name):
    """Load a module using its name and return the module object."""
    import importlib.util
    spec = importlib.util.find_spec(name)
    module = import

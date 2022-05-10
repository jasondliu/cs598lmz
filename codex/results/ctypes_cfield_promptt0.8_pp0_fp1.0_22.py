import ctypes
# Test ctypes.CField is working on both Python 2 and Python 3.
# On Python 3, ctypes is not defined as a package at the top level.
# You get the following:
#   TypeError: 'module' object is not callable
# if you don't test that ctypes exists as a package.
if not isinstance(ctypes, types.ModuleType):
    raise AssertionError("ctypes is not a module")

if not hasattr(ctypes, 'CField'):
    # This is a workaround for Python 2.
    # On Python 2, you need the following:
    #     from ctypes import CField
    # to use the class.
    # This does not work on Python 3.
    # On Python 3, you need to do this instead:
    #     from ctypes import _CData
    #     from _ctypes import CField
    from _ctypes import CField

# -----------------------------------------------------------------------------
# The following functions are used for testing the ctypes module.
# -----------------------------------------------------------------------------
def _build_simple_struct_type(name, field_names):
    """
    Build a simple ctypes

import ctypes
ctypes.cast(0, ctypes.py_object).value

# The instancemethod type is a builtin, but is not accessible from __builtins__
import types
types.InstanceType
# But not in __builtins__
'InstanceType' in globals()

# Test ctypes callback
import _ctypes_test
callback = _ctypes_test.set_callback(lambda x: x)

# Test the PEP 445 ImportError fix
import test.pep445_import_fix
test.pep445_import_fix.test_pep445_import_fix()

# Test METH_FASTCALL
import _ctypes_test
_ctypes_test.call_fastcall_func.restype = None

_ctypes_test.call_fastcall_func()

# Test set_conversion_mode
import _ctypes
_ctypes.set_conversion_mode("ascii", "strict")
# "ascii" is not a valid error handler
try:
    _ctypes.set_conversion_mode("ascii", "ignore")


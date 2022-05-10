import ctypes
# Test ctypes.CFUNCTYPE

import _ctypes_test

def callback(arg):
    print('callback', arg)

CALLBACK = ctypes.CFUNCTYPE(None, ctypes.py_object)

# Call a C callback
_ctypes_test.set_callback(CALLBACK(callback), 42)
_ctypes_test.call_callback_now(42)

# Make a ctypes function point to a C callback
f = ctypes.CFUNCTYPE(None, ctypes.py_object)(_ctypes_test.get_callback())
f(42)

# Call a C callback stored in a ctypes data field
class X(ctypes.Structure):
    _fields_ = [('callback', CALLBACK)]
inst = X()
inst.callback = CALLBACK(callback)
inst.callback(42)

# Pass around a C callback stored in a ctypes data field
inst.callback = CALLBACK(_ctypes_test.get_callback())

# Callback from a callback from Python
def callback2(arg):
    print('callback2')
    callback

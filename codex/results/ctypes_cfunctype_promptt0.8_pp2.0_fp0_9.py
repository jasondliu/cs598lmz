import ctypes
# Test ctypes.CFUNCTYPE
import _ctypes_test
printf = _ctypes_test.printf
CallbackType = ctypes.CFUNCTYPE(None)

def py_callback(*args):
    print('py_callback:', args)

printf(b'printf from c: %s\n', b'Hello World')

cb = CallbackType(py_callback)
printf(b'printf from c: %d\n', b'42', cb)
cb()

cb = CallbackType(lambda: None)
printf(b'printf from c: %d\n', b'42', cb)
cb = CallbackType(lambda x: None)
printf(b'printf from c: %d\n', b'42', cb)
cb(1)
cb = CallbackType(lambda x, y: None)
printf(b'printf from c: %d\n', b'42', cb)
cb(1,2)
cb = CallbackType(lambda x, y, z: None)
printf(b'printf from c: %d\n', b'42',

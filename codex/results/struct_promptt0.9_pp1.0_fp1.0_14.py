import _struct
# Test _struct.Struct
print '_struct.unpack(b"i", bytes):', _struct.unpack(b'i', b'\1\0\0\0')
# Test ctypes.cdll.LoadLibrary
import ctypes
# Test ctypes.Structure
class TestStuct(ctypes.Structure):
    _fields_ = [('a', ctypes.c_int), ('b', ctypes.c_int)]
teststruct = TestStuct(1, 2)
teststruct.c = 3
if not hasattr(teststruct, 'c'):
    raise RuntimeError
print "teststruct: %s, %d" % (teststruct, teststruct.a)

# Test _weakref.ref()
import _weakref
ref = _weakref.ref(teststruct)
if ref() is None:
    raise RuntimeError
# Test _weakrefset
set = _weakref.WeakSet([teststruct])
if teststruct not in set:
    raise RuntimeError
# Test builtin.type
if not isinstance(set, type(type)):
    raise RuntimeError


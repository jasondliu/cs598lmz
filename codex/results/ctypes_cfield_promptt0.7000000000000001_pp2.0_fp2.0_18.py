import ctypes
# Test ctypes.CField
class X(ctypes.Structure):
    _fields_ = [("a", ctypes.c_int)]
x = X()
print x.a

# Check that ctypes.CField is unpickled correctly
import pickle
x = pickle.loads(pickle.dumps(x))
print x.a
</code>


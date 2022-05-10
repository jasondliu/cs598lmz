import ctypes
# Test ctypes.CField instance without assignment_decorator
f = ctypes.CField("field", ctypes.c_int, 0)
# Force late binding to call __init__
hasattr(f, "offset")
```

```
# cpython/Lib/test/test_ctypes/test_field_with_pystruct.py
import ctypes
# Test ctypes.CField overriding struct member name
f = ctypes.CField("int_field", ctypes.c_int, 0)
@f.assignment_decorator
class PyStruct(ctypes.Structure):
    pass
# Force late binding to call __init__
print(ctypes.memset(ctypes.addressof(PyStruct()), 0, ctypes.sizeof(PyStruct)))
```

```
# cpython/Demo/memoryview/pymemview.py
# Legitimate use of CField.__init__
# as recorded in http://bugs.python.org/issue15356
import ctypes
class Pymemview(ctypes.Structure):
    _fields_ = [

import ctypes
ctypes.cast(None, ctypes.py_object)  # assert error

# Verify initialization to NULL.
import ctypes
ctypes.py_object()

# Test py_object(None)
import ctypes
ctypes.py_object(None)

# Test py_object(py_object(None))
import ctypes
ctypes.py_object(ctypes.py_object(None))

# Test py_object(py_object(obj))
import ctypes
ctypes.py_object(ctypes.py_object(42))

# Test py_object(obj)
import ctypes
ctypes.py_object(42)

# Test cast to py_object
import ctypes
ctypes.cast(b'abcde', ctypes.py_object)

# Test cast from py_object
import ctypes

import ctypes
ctypes.cast(0, ctypes.py_object)

# SEGV
import ctypes
ctypes.cast(0, ctypes.py_object).value

# SEGV
import ctypes
ctypes.cast(0, ctypes.py_object).value = None

# SEGV
import ctypes
ctypes.cast(0, ctypes.py_object).ob_refcnt = 0

# SEGV
import ctypes
ctypes.cast(0, ctypes.py_object).ob_refcnt = -1

# SEGV
import ctypes
ctypes.cast(0, ctypes.py_object).ob_refcnt = 0xffffffff

# SEGV
import ctypes
ctypes.cast(0, ctypes.py_object).ob_refcnt = 0xffffffffffffffff

# SEGV
import ctypes
ctypes.cast(0, ctypes.py_object).ob_refcnt = 0xffffffffffffffffffffffffffffffff

# SEGV
import ctypes
ctypes.

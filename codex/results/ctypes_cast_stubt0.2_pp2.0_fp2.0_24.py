import ctypes
ctypes.cast(0, ctypes.py_object)

# Test for issue #1202
import ctypes
ctypes.cast(0, ctypes.py_object).value

# Test for issue #1203
import ctypes
ctypes.cast(0, ctypes.py_object).value = None

# Test for issue #1204
import ctypes
ctypes.cast(0, ctypes.py_object).value = 0

# Test for issue #1205
import ctypes
ctypes.cast(0, ctypes.py_object).value = 0.0

# Test for issue #1206
import ctypes
ctypes.cast(0, ctypes.py_object).value = ""

# Test for issue #1207
import ctypes
ctypes.cast(0, ctypes.py_object).value = ()

# Test for issue #1208
import ctypes
ctypes.cast(0, ctypes.py_object).value = []

# Test for issue #1209
import ctypes
ctypes.cast(0, ctypes.py_object).value

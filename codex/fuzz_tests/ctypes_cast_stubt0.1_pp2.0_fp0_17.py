import ctypes
ctypes.cast(0, ctypes.py_object).value

# This is a hack to get around the fact that the Python 2.7.3
# interpreter crashes on exit when this test runs.
import os
os._exit(0)

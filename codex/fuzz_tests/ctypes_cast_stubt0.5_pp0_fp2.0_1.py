import ctypes
ctypes.cast(None, ctypes.py_object)

# and this is what I need to do to get it to work
import ctypes
ctypes.cast(None, ctypes.py_object).value

# this is what I would like to do
from ctypes import py_object
py_object.from_param(None).value
</code>


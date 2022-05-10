import ctypes
ctypes.cast(0, ctypes.py_object).value

# This is a more general way of getting the value of an object.
# However, it will not work if the object is a builtin type.
import sys
sys.getrefcount(0)

# This is a more general way of getting the value of an object.
# However, it will not work if the object is a builtin type.
import gc
gc.get_referents(0)

# This is a more general way of getting the value of an object.
# However, it will not work if the object is a builtin type.
import inspect
inspect.getclasstree([0])

# This is a more general way of getting the value of an object.
# However, it will not work if the object is a builtin type.
import sys
sys.getobjects(0)

# This is a more general way of getting the value of an object.
# However, it will not work if the object is a builtin type.
import sys
sys.getallocatedblocks()

# This is a more general way of getting

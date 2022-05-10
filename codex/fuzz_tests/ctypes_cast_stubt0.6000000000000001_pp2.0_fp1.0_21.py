import ctypes
ctypes.cast(id(object), ctypes.py_object).value

# 方法2
__import__('sys').getrefcount(object)

# 方法3
from sys import getrefcount
import gc
def ref_count(address):
    return getrefcount(ctypes.cast(address, ctypes.py_object).value)
ref_count(id(object))

# 方法4
import weakref
def ref_count(address):
    return len(gc.get_referrers(ctypes.cast(address, ctypes.py_object).value))
ref_count(id(object))

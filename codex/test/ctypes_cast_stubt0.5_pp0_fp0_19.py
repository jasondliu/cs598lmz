import ctypes
ctypes.cast(None, ctypes.py_object)

# The following import is needed to make the
# "from . import _distributor_init" work in
# tensorflow/python/ops/distributions/__init__.py

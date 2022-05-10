import ctypes
ctypes.cast(0, ctypes.py_object)

# This is a hack to force the object mode runtime to be loaded,
# otherwise the test_ctypes test fails.
import _ctypes

# This is a hack to force the object mode runtime to be loaded,
# otherwise the test_ctypes test fails.

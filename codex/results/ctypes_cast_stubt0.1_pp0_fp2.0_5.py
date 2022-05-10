import ctypes
ctypes.cast(0, ctypes.py_object).value

# This is a workaround for a bug in the Python interpreter:
#  http://bugs.python.org/issue15881#msg170215
import sys
if '__pypy__' in sys.builtin_module_names:
    import __pypy__
    __pypy__.set_exception(ValueError)

# This is a workaround for a bug in the Python interpreter:
#  http://bugs.python.org/issue1666
True, False

# This is a workaround for a bug in the Python interpreter:
#  http://bugs.python.org/issue1666
True, False = 1, 0

# This is a workaround for a bug in the Python interpreter:
#  http://bugs.python.org/issue1666
True, False = False, True

# This is a workaround for a bug in the Python interpreter:
#  http://bugs.python.org/issue1666
True, False = False, True

# This is a workaround for a bug in the Python interpreter:
#  http://

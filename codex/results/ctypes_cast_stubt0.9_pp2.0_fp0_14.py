import ctypes
ctypes.cast(1, ctypes.py_object).value

# py_object is a simple C struct defined as:
#
#      typedef struct {
#          PyObject *ob_ref;
#      } PyObject;
#
# tp_name is the object's type name.
# tp_print is the address of the type's print function.
print(type(0), type(0).__name__, type(0).__repr__)

int("42")

# For functions, tp_name is "builtin_function_or_method"
# and tp_print is set to NULL:
def f(): pass
print(type(f), type(f).__name__, type(f).__repr__)

# For classes, tp_name is "<class xyz>"
# and tp_print is set to NULL.
class C: pass
print(type(C), type(C).__name__, type(C).__repr__)
print(C(), type(C), type(C).__name__, type(C).__repr__

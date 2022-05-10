import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_void_p, ctypes.c_char_p, ctypes.c_int, ctypes.c_int, ctypes.c_double)

def _callback(userdata, typ, code, msg, value):
    print("userdata =", userdata)
    print("type =", typ)
    print("code =", code)
    print("msg =", msg)
    print("value =", value)
    print("")

callback = FUNTYPE(_callback)

# We must keep a reference to MyCallbackType instance
# in order to prevent its refcount to go to zero which
# causes segfault on some platforms
_ctypes_callback_instance = callback

# Create the C++ side class
class_ = cppimport.imp("struct_")

# Create an instance of the C++ class
instance = class_.new()

# Call the C++ class method that takes a callback
instance.call_callback(callback, b"Hello World")

# Call the C++ class method that takes a callback and a void*
instance.call_callback_

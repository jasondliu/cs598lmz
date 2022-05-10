import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    print("hello world")
    return None

# Then, we specify the name of the function, and its arguments (if any)
# In this example, the extension function takes no arguments and returns an int
ext.add_function("fun", fun)

# We then load the extension and call the function
mod = ext.load_extension()
mod.fun()

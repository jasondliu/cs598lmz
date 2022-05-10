import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello world"
# initialize the library
lib = ctypes.CDLL(os.path.abspath("libfoo.so"))
lib.return_hello_world.restype = ctypes.py_object
# call the function
print(lib.return_hello_world())
# call the function pointer
print(fun())

# call the function pointer
print(lib.return_hello_world_ptr()())
</code>
gives
<code>b'hello world'
hello world
hello world
</code>


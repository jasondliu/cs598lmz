import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

# Set up test data
a = 6
b = 7

# Call Rust function from Python
lib.add.restype = ctypes.c_int
r = lib.add(a, b)
print(r)

# Call Rust function from Python (with wrapper)
@FUNTYPE
def my_add(x, y):
    return x + y
lib.add2.restype = ctypes.c_int
r = lib.add2(a, b, my_add)
print(r)

# Call Python function from Rust
r = lib.call_py_function(a, b)
if r != 13:
    print('Rust code not working!')
else:
    print('Calling Python from Rust is working')

# Call Rust from Python
r = lib.call_rust_function(a, b)
if r != 13:
    print('Python wrapper code not working!')
else:
    print('Calling Rust from Python is working')

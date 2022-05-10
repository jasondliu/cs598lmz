import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.c_int)

def callback(a, b):
    print("callback called with %d and %d" % (a, b))
    return a + b

if __name__ == "__main__":
    lib = ctypes.CDLL("libtest.so")
    lib.set_callback(FUNTYPE(callback))
    print("2 + 3 = %d" % lib.run_callback(2, 3))
</code>
Compile the shared library:
<code>gcc -shared -fPIC -o libtest.so test.c
</code>
Run the Python code:
<code>$ python3 test.py 
callback called with 2 and 3
2 + 3 = 5
</code>


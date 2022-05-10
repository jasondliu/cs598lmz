import ctypes
# Test ctypes.CFUNCTYPE with an empty parameter list.
def my_print():
    print("Hello World")

print("First test")
CMPFUNC=ctypes.CFUNCTYPE(None)
hello_func=CMPFUNC(my_print)
hello_func()
print("Second test")
hello_func=CMPFUNC(lambda : print("Hello World"))
hello_func()
print("Third test")
hello_func()
print("Tests done")
</code>

First test
Hello World
Second test
Hello World
Third test
Hello World
Tests done

<code>CMPFUNC=ctypes.CFUNCTYPE(None, ctypes.c_void_p)
</code>

First test
Hello World
Second test
Hello World
Third test
Hello World
Tests done

<code>CMPFUNC=ctypes.CFUNCTYPE(None, ctypes.c_void_p, ctypes.c_uint)
</code>

First test
Hello World
Second test
Hello World
Third test
Hello World
Tests

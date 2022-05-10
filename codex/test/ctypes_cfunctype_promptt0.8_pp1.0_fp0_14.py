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

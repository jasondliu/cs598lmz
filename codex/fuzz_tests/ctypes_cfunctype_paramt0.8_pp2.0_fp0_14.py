import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_int))

def cb_func(arg):
    print(arg[0])
    return 0

# C callback function
c_cb_func = FUNTYPE(cb_func)

# Python callback function
def cb_func2():
    print('callback')

# C callback function
c_cb_func2 = FUNTYPE(cb_func2)

# create instance of the class
my_object = MyClass()

# call the method
my_object.callback(c_cb_func)

# call the method
my_object.callback2(c_cb_func2)

# wait for input
input("Press ENTER to continue...")

# call callback again, this should crash
my_object.callback(c_cb_func)
</code>
This is the output:
<code>ctypes.CPythonAPI object at 0x000001A7FBA0C040&gt;
callback
Traceback (most recent call last):
  File "E:\Repositories\

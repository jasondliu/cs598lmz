import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return "hello"
# declare a function pointer type
FUNPTR = ctypes.CFUNCTYPE(ctypes.c_char_p)
class MyClass(object):
    def __init__(self, fptr):
        self.fptr = fptr

    # define a member function which takes a function pointer as argument
    def callfunc(self):
        # call the function pointed to by The instance's "fptr" attribute
        return self.fptr()

# create an instance of MyClass
myinstance = MyClass(fun)

# call the member function of the instance

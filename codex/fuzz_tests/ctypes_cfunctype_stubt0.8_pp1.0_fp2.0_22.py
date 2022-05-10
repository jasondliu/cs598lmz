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
print myinstance.callfunc()
</code>
The above code does not print <code>hello</code>; instead I get the following error:
<code>ArgumentError: argument 1: &lt;type 'exceptions.TypeError'&gt;: wrong type
</code>
I couldn't find a proper example to pass a Python function as a C function pointer. Can anyone tell me what I am doing wrong here?


A:

The problem here is that <code>MyClass.callfunc()</

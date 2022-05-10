import ctypes
FUNTYPE = ctypes.CFUNCTYPE(None, [])
@FUNTYPE
def my_python_func(value1):
    print("value1=", value1)
my_python_func(1)
my_python_func(3)
my_python_func(12)
my_python_func(None)
my_python_func("toto")
my_python_func(78.12)
</code>
but if so I think that I will have to duplicate the code to be called and the logic to decide which code to call ... it seems to me an ugly solution:
<code>def my_python_func(value1):
    value1 = ctypes.cast(value1)
    if isinstance(value1):
        print("value1=", value1)
    elif isinstance(value2):
        pass
    else: 
        pass 
    ....
my_python_func(1)
my_python_func(3)
my_python_func(12)
my_python_func(78.12)
</code>


A:

You're basically asking to be able to use

import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 1
f = fun
print(f())
f = None
print(fun())#crash
</code>
question:
when you assign a ctypes created function to a variable and then the variable is None, the function in memory is not destroyed.
why is this happening?


A:

Name are just refferance to object. 
In your code you are creating object named <code>fun</code>, and <code>f</code> is just a refference to that object. You cannot destroy object by removing refference.
You can use <code>del fun</code> to remove that object(variable). But again, its reference is saved in <code>f</code>


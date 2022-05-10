import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double, ctypes.c_double)
def make_function(body):
    string = 'lambda x,y: %s' % body
    print(string)
    func = eval(string)
    return FUNTYPE(func)

def function(x,y):
    return x+2*y

f = make_function(function)

print(f(1,2))
</code>
When we run the code, the python console shows:
<code>lambda x,y: &lt;function function at 0x7f996902b268&gt;
9.0
</code>
and the Python GUI console shows:
<code>lambda x,y: &lt;function function at 0x7f59f0b9b268&gt;
Traceback (most recent call last):
  File "./test.py", line 14, in &lt;module&gt;
    print(f(1,2))
TypeError: '_CFuncPtr' object is not callable
</code>
Why is the Python

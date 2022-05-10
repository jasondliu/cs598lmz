import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def pyfunc(x):
    return x + 1

pyfunc_ptr = FUNTYPE(pyfunc)

print pyfunc_ptr(1)
print pyfunc_ptr(2)
</code>
I get the following error:
<code>Traceback (most recent call last):
  File "test.py", line 10, in &lt;module&gt;
    print pyfunc_ptr(1)
TypeError: 'CFUNCTYPE' object is not callable
</code>
What is the correct way to do this?


A:

<code>CFUNCTYPE</code> is a factory for creating <code>CFunctionType</code> instances.
<code>pyfunc_ptr = FUNTYPE(pyfunc)
</code>
should be
<code>pyfunc_ptr = FUNTYPE(pyfunc)()
</code>


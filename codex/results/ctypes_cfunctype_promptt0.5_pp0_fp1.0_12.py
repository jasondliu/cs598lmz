import ctypes
# Test ctypes.CFUNCTYPE callback
def callback(value):
    print('Called back with value', value)

CALLBACKFUNC = ctypes.CFUNCTYPE(None, ctypes.c_int)

# Create an instance of CALLBACKFUNC
c_callback = CALLBACKFUNC(callback)
</code>
I am getting an error:
<code>TypeError: 'CFUNCTYPE' object is not callable
</code>
How can I call <code>CALLBACKFUNC</code>?


A:

Your code is correct.  The error is because <code>CALLBACKFUNC</code> is a type, not a function.  You need to make an instance of that type, not call it.
<code>&gt;&gt;&gt; CALLBACKFUNC
&lt;class 'ctypes.CFUNCTYPE'&gt;
&gt;&gt;&gt; CALLBACKFUNC(callback)
&lt;CFUNCTYPE(None, c_int) object at 0x7f624b0a1d08&gt;


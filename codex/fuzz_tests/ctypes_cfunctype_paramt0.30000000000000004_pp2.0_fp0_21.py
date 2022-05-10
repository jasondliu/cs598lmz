import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)

def callback(x):
    print "callback called with", x
    return x

# convert function to CFUNCTYPE
cbfunc = FUNTYPE(callback)

# call function
cbfunc(42)
</code>
This works fine. However, if I try to pass the <code>callback</code> function to another function, I get an error:
<code>def callback(x):
    print "callback called with", x
    return x

# convert function to CFUNCTYPE
cbfunc = FUNTYPE(callback)

def call_callback(cb):
    cb(42)

# call function
call_callback(cbfunc)
</code>
This gives me the following error:
<code>Traceback (most recent call last):
  File "test.py", line 14, in &lt;module&gt;
    call_callback(cbfunc)
  File "test.py", line 12, in call_callback
    cb(42)
TypeError: 'CFUNCTYPE

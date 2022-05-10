import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
def myfun(n):
    print n
    return n
CALLBACK = FUNTYPE(myfun)

# Install the callback
lib.set_callback(CALLBACK)  # Success!

# Now when the callback is called it works as expected
&gt;&gt;&gt; lib.call_callback()
8   # This is printed by myfun()
8   # This is the return value of call_callback()
</code>


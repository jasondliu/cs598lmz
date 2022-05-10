import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
</code>
Then, you can instantiate your function and use it at any time.
<code>counter = FUNTYPE(lambda x: x + 1)
counter(2)
</code>
Output:
<code>3
</code>


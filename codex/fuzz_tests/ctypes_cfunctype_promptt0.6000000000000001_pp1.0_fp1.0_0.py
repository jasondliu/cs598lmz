import ctypes
# Test ctypes.CFUNCTYPE()

# This one works:
#func = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)(lambda x: x + 1)

# This one gives a segfault:
func = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)(lambda x: x + 1)

print(func(7))
</code>
If you run the code above, you will get a segfault.
Why is that?
I think it is because of the way the <code>__call__</code> method of <code>ctypes.CFUNCTYPE</code> is implemented.
<code>def __call__(self, *args):
    return self(args)
</code>
I think the <code>self(args)</code> should be <code>self.__call__(args)</code> instead.
What do you think?


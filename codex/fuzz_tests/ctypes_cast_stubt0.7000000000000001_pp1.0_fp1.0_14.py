import ctypes
ctypes.cast(None, ctypes.c_int)
</code>
Expected output:
<code>&lt;class 'ctypes.c_int'&gt;
</code>
Actual output:
<code>&lt;class 'ctypes.c_void_p'&gt;
</code>
I've looked through the documentation and I can't find any way of doing this. Is this possible in Python with ctypes?


A:

The <code>ctypes.cast</code> function doesn't create an instance of the specified type, but returns a new object that is a pointer to the original object.  This is similar to the C cast operator.
You can use the <code>ctypes.POINTER</code> type to create a pointer to an object at runtime.  For example:
<code>&gt;&gt;&gt; ctypes.POINTER(ctypes.c_int)(None)
&lt;class 'ctypes.c_int'&gt;
</code>


import ctypes
ctypes.cast(obj, ctypes.py_object).value
</code>
So, if you wanted to get the value of the object at the address <code>0x7fffffffdaa8</code>, you could do something like this:
<code>&gt;&gt;&gt; import ctypes
&gt;&gt;&gt; ctypes.cast(ctypes.c_void_p(0x7fffffffdaa8), ctypes.py_object).value
0
</code>
You can also use the <code>id()</code> function to get the address of an object.
<code>&gt;&gt;&gt; id(0)
140735688095168
&gt;&gt;&gt; ctypes.cast(ctypes.c_void_p(140735688095168), ctypes.py_object).value
0
</code>


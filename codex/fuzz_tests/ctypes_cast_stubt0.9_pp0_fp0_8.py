import ctypes
ctypes.cast(2, ctypes.py_object).value = 3.
</code>
But that doesn't change the int to a float (I only get a TypeError or a core dump). 
I've been trying similar things in the repl, but so far had no luck. Can you convert an int or a Long to a Float in ironpython? If so how?


A:

It can't be done directly, you will have to create a new <code>float</code> object.  You can convert to a double first:
<code>&gt;&gt;&gt; double(long(6))
6.0
</code>
Or simply:
<code>&gt;&gt;&gt; float(long(6))
6.0
</code>


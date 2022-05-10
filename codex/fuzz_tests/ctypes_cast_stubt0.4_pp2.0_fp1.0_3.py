import ctypes
ctypes.cast(0, ctypes.py_object).value

# This is the error I get:
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
&lt;ipython-input-10-d8c1d9e9e9f7&gt; in &lt;module&gt;()
----&gt; 1 ctypes.cast(0, ctypes.py_object).value

AttributeError: 'NoneType' object has no attribute 'value'
</code>
I'm not sure what I'm doing wrong. I'm running Python 3.5.2 on Ubuntu 16.04.


A:

The <code>ctypes.cast</code> function returns <code>None</code> for invalid cast operations.
The problem is that you can't cast <code>0</code> to <code>ctypes.py_object</code>.
<code>&gt;&gt;&gt; ctypes.cast(0, ctypes.py_object)
&gt;&gt;&gt; ctypes.cast(1, ctypes.py_object)
&lt;__main

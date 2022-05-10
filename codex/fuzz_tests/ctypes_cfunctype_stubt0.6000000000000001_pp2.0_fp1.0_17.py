import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return 1

print(fun())
</code>
This gives the following error:
<blockquote>
<pre><code>&lt;code&gt;Traceback (most recent call last):
  File "t.py", line 5, in &amp;lt;module&amp;gt;
    print(fun())
WindowsError: exception: access violation reading 0x00000008
&lt;/code&gt;</code></pre>
</blockquote>
What is wrong?


A:

The <code>fun()</code> function returns a <code>c_long</code> value, not a Python object.  You need to convert that to a Python object:
<code>print(ctypes.pythonapi.PyInt_FromLong(fun()))
</code>


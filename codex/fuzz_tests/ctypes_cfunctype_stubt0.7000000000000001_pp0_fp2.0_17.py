import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return None

fun()
</code>
Then it raises the exception:
<code>TypeError: Don't know how to convert parameter 0
</code>
This is very unexpected because Python's ctypes documentation says:
<blockquote>
<p>Return value: None, c_void_p(None) or equivalent</p>
</blockquote>
And it mentions <code>None</code> here.
Is this a bug? How to use <code>None</code> as a return value?


A:

<code>None</code> is a keyword in Python. It is not a type. <code>None</code> is a special value which is returned by some functions and methods.
So, when you write this line:
<code>FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
</code>
<code>None</code> is not a type. You are not saying <code>return None</code>. You are saying <code>return &lt;undefined value&gt;</code>.
If you want to return <code>None</code> from

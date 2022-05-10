import ctypes

class S(ctypes.Structure):
    _fields_ = [('x', ctypes.c_int)]

ctypes.CField = type(S.x)
type(S.x)
ctypes.CField.__get__(S())
</code>
This returns <code>S.x</code>, but not <code>S.x.__get__(S())</code>
How to rewrite this code to get <code>ctypes.c_int(0)</code> ?


A:

It's a descriptor, invoke <code>__get__</code>.
<code>&gt;&gt;&gt; ctypes.CField.__get__(S(), None)
0
</code>
<blockquote>
<p>So I have to manually pass S()? Is it possible to create a new type (call it Field) that automatically pass value instance to __get__ invocation?</p>
</blockquote>
If <code>S</code> is the type, <code>S()</code> is an instance of <code>S</code>.  You'd need a descriptor class that knows about the <code>type</code> or a function to invoke.  You can't simply attach a callback to <code>__get__</code>,

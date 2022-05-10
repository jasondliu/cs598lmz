import ctypes
FUNTYPE = ctypes.CFUNCTYPE(ctypes.py_object)
@FUNTYPE
def fun():
    return u"Hello"
</code>
The following prints <code>u'Hello'</code>, as expected:
<code>print fun()
</code>
But the following prints <code>Hello</code> without the <code>u</code>:
<code>print fun.__call__()
</code>
What is the <code>__call__</code> method doing differently from the call syntax?
How do I make it so that <code>__call__</code> returns the <code>u</code>?


A:

<code>__call__</code> is just a method, it doesn't give any special treatment to the return value.  The issue is that <code>ctypes</code> is returning a plain string, not a unicode string.
<code>print type(fun()), 'u'+fun()
print type(fun.__call__()), 'u'+fun.__call__()
</code>
outputs
<code>&lt;type 'unicode'&gt; uHello
&lt;type 'str'&gt; uHello
</

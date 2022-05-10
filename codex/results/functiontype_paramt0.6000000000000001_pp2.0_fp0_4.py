from types import FunctionType
list(FunctionType('', '', '', (), None, None, None, None))
[<code object &lt;module&gt; at 0x7f17c5c1f200, file "&lt;stdin&gt;", line 1&gt;, None]
</code>
In Python 3.4, the <code>__code__</code> attribute is a read-only attribute, so you can't do this:
<code>&gt;&gt;&gt; def f():
...     pass
... 
&gt;&gt;&gt; f.__code__ = 'foo'
Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
AttributeError: readonly attribute
</code>
You can still do it on Python 3.4, but you have to do it via <code>ctypes</code> (this is on a 64-bit Linux machine):
<code>&gt;&gt;&gt; import ctypes
&gt;&gt;&gt; f = lambda: None
&gt;&

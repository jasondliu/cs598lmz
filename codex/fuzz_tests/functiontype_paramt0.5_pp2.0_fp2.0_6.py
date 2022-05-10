from types import FunctionType
list(FunctionType(lambda: None).__dict__.keys())

# ['__annotations__', '__call__', '__closure__', '__code__', '__defaults__', '__get__', '__globals__', '__kwdefaults__', '__name__', '__qualname__']
</code>
However, when I try to access the <code>__code__</code> attribute, I get:
<code>&gt;&gt;&gt; FunctionType(lambda: None).__code__
Traceback (most recent call last):
  File "&lt;stdin&gt;", line 1, in &lt;module&gt;
TypeError: 'code' object is not subscriptable
</code>

This is the same for any function, e.g. <code>FunctionType(print).__code__</code> also results in a <code>TypeError</code>.
I'm running Python 3.6.3 on Windows 10.

Why can't I access the <code>__code__</code> attribute?


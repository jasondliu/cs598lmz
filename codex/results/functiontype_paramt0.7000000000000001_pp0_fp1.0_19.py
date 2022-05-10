from types import FunctionType
list(FunctionType(f.__code__, f.__globals__, name=f.__name__,
                   argdefs=f.__defaults__, closure=f.__closure__)
     for f in [lambda x, y=2: x + y, lambda x, y, z=3: x + y + z]]
</code>
[<code>&lt;function &lt;lambda&gt; at 0x7f8b8d2c2d90&gt;, &lt;function &lt;lambda&gt; at 0x7f8b8d2c2e60&gt;]
The <code>inspect</code> module can give you a lot more information, for example:
<code>import inspect
inspect.getsource(f)
</code>
'def f(x, y=2):\n    return x + y\n'
<code>inspect.getargspec(f)
</code>
ArgSpec(args=['x', 'y'], varargs=None, keywords=None, defaults=(2,))
<code>inspect.

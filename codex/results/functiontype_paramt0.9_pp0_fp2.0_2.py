from types import FunctionType
list(FunctionType(FunctionType(lambda x:(x+2))(2)).__closure__[0].cell_contents)

()
</code>
It's a bit of a mess, so I tried to extract the <code>__closure__</code>:
<code>def innermost(fn):
    if isinstance(fn.__closure__, FunctionType):
        return innermost(fn.__closure__)
    return fn.__closure__

innermost(FunctionType(FunctionType(lambda x:(x+2))(2)))
</code>
But you can't assign a function to a variable if the function has a closure:
<code>&gt;&gt;&gt; fn = FunctionType(FunctionType(lambda x:(x+2))(2))
&gt;&gt;&gt; innermost(fn)
(&lt;cell at 0x101dc1ab8: int object at 0x1016e5558&gt;,)
&gt;&gt;&gt; fn2 = FunctionType(fn(2))
Traceback (most recent call last):
  File "&lt;pys

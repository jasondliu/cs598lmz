from types import FunctionType
list(FunctionType(lambda x:x+1,{}).__dict__.items())

# Output:
[('__doc__', None),
 ('__globals__', {}),
 ('__code__', &lt;code object &lt;lambda&gt; at 0x1033c0b30, file "&lt;stdin&gt;", line 1&gt;),
 ('__name__', '&lt;lambda&gt;'),
 ('__annotations__', {})]
</code>
As you can see the <code>__globals__</code> attribute is the dictionary in which the function is created.
Also, because this attribute is <code>mutable</code>, you can change it after creation using:
<code>f.__globals__ = {'a': 10}
</code>


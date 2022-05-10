from types import FunctionType
list(FunctionType(f.__code__, None, f.__name__, f.__defaults__, f.__closure__))
</code>
This produces the following output:
<code>[&lt;cell at 0x10d39abe8: str object at 0x10d3af2e0&gt;, &lt;cell at 0x10d39af28: str object at 0x10d3af2a0&gt;, &lt;cell at 0x10d39af48: str object at 0x10d3af3d0&gt;, &lt;cell at 0x10d39ad28: list object at 0x10d3af568&gt;]
</code>
which is pretty much what <code>inspect.getclosurevars(f).cells</code> yields:
<code>{'a': &lt;cell at 0x10d39abe8: str object at 0x10d3af2e0&gt;, 'b': &lt;cell at 0x10d39af28: str object at 0x10d3af2a0&gt;, '

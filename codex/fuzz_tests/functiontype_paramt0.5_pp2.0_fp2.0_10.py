from types import FunctionType
list(FunctionType(a.__code__, a.__globals__, a.__name__, a.__defaults__, a.__closure__)
     for a in [lambda x: x, lambda _: None])
# [<function &lt;lambda&gt; at 0x7f8b2e7b2f28&gt;, &lt;function &lt;lambda&gt; at 0x7f8b2e7b2ea0&gt;]
</code>


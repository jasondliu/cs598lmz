from types import FunctionType
list(FunctionType(f.__code__, f.__globals__, name=f.__name__, argdefs=f.__defaults__, closure=f.__closure__)
     for f in [f1, f2]
)
</code>

<code>[&lt;function f1 at 0x0000027FC7D66620&gt;, &lt;function f2 at 0x0000027FC7D66C80&gt;]
</code>


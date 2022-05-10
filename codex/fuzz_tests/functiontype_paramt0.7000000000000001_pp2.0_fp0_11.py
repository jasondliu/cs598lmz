from types import FunctionType
list(FunctionType(f.__code__, f.__globals__, name=f.__name__,
                  argdefs=f.__defaults__,
                  closure=f.__closure__) for f in (func, func1))
</code>
<code>[&lt;function __main__.func()&gt;, &lt;function __main__.func1()&gt;]
</code>


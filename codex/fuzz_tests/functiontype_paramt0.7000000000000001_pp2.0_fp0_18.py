from types import FunctionType
list(FunctionType(f.__code__,globals(),'new',f.__defaults__,f.__closure__))
</code>
It is easy to see that <code>f.__code__</code> and <code>f.__closure__</code> are the same, but <code>f.__defaults__</code> is not. Why?


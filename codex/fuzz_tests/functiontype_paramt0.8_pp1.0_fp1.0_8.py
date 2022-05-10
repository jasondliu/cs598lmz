from types import FunctionType
list(FunctionType(f.__code__, f.__globals__, f.__name__, f.__defaults__, f.__closure__).__dict__)
</code>
Note that this approach won't work with all decorated functions, since it only works if the inner function is returned from the outer function. It's also impossible to preserve the return value of the inner function if the outer function has a <code>return</code> statement anywhere in it's body (or one of it's own inner functions).


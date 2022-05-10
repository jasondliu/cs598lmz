from types import FunctionType
list(FunctionType(f.__code__, {}, "some_name", f.__defaults__, f.__closure__))

# Or, a little more general, but still ugly:
list(f.__code__.co_freevars)
</code>


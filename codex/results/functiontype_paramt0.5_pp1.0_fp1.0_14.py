from types import FunctionType
list(FunctionType(lambda: None, globals(), "").__code__.co_freevars)

# Output:
# ['__name__', '__doc__', '__package__', '__loader__', '__spec__', '__annotations__', '__builtins__', '__file__', '__cached__', '__builtin_module_names__']
</code>
<code>co_freevars</code> is a tuple containing the names of the free variables used in the function.


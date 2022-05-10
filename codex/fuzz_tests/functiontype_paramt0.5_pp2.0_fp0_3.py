from types import FunctionType
list(FunctionType(lambda x: x, globals(), 'lambda'))
</code>
<code>__annotations__</code> is a dictionary of type annotations for the function's parameters and the return value.
<code>__closure__</code> is a tuple of cell objects (which are themselves tuples of two elements) containing the closed-over variables.
<code>__code__</code> is the function's code object.
<code>__defaults__</code> is a tuple of default values for the function's parameters.
<code>__dict__</code> is a dictionary containing the function's attributes.
<code>__doc__</code> is the function's docstring.
<code>__globals__</code> is a dictionary containing the function's global variables.
<code>__name__</code> is the function's name.
<code>__qualname__</code> is the function's qualified name.


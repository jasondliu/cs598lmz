from types import FunctionType
list(FunctionType(foo, globals())())
</code>
The <code>globals()</code> function is the same as the <code>globals</code> builtin, except that it's a function instead of a builtin.


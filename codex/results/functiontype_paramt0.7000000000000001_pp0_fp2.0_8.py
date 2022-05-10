from types import FunctionType
list(FunctionType(func).__code__.co_varnames)
</code>
returns the names of the local variables of the function <code>func</code> as a list.
<code>list(FunctionType(func).__code__.co_freevars)
</code>
returns the names of the free variables of the function <code>func</code> as a list.
<code>list(FunctionType(func).__code__.co_cellvars)
</code>
returns the names of the local variables that are referenced by nested functions as a list.


from types import FunctionType
list(FunctionType(l.func_code, l.func_globals , l.func_name, l.func_defaults, l.func_closure))
</code>
In the <code>types</code> package, a <code>FunctionType</code> object is defined as:
<code>FunctionType(code, globals[, name[, argdefs[, closure]]])
</code>
When creating a function with this function, the closure is a parameter that we can specify, so if we want to make a clone of an old function with a new closure, it is quite straightforward to do.


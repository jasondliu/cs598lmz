from types import FunctionType
list(FunctionType(f.func_code, f.func_globals))
</code>
It's the same as:
<code>list(f)
</code>
But I don't know what is the meaning of <code>f.func_code</code> and <code>f.func_globals</code>.


A:

<code>func_code</code> and <code>func_globals</code> are attributes of function objects.  They are used to create new function objects, as in your example.
<code>func_code</code> is a code object, the compiled bytecode of the function.  <code>func_globals</code> is a dictionary object containing the global namespace (or closure) of the function.


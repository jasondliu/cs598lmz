from types import FunctionType
list(FunctionType(f.func_code, f.func_globals, f.func_name, f.func_defaults, f.func_closure) for f in [lambda: None, lambda: None])
</code>
<blockquote>
<p>TypeError: type 'function' is not an acceptable base type</p>
</blockquote>
Note that <code>FunctionType</code> is a class, not a function.


A:

<code>FunctionType</code> is the type of all functions, so you can't use it to instantiate new functions.  You can use <code>types.FunctionType</code> to create a function, but it is not easy to use.  You need to provide a <code>code</code> object for the function body, and a <code>globals</code> mapping for the global variables the function can access, and a name, and possibly other arguments.  You can get a <code>code</code> object by calling <code>compile</code> on a string of Python code.  Here is an example:
<code>import types

def make_function

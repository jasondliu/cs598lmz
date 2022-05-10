from types import FunctionType
list(FunctionType(f.__code__, globals(), 'baz')())
# ['baz']
</code>
The way this works is by creating a new function from the function's <code>__code__</code> object, which is the compiled bytecode for the function. This object has a number of attributes, of which the most relevant ones are:

<code>co_argcount</code>: The number of arguments the function accepts.
<code>co_varnames</code>: A tuple of the names of the arguments and local variables.
<code>co_cellvars</code>: A tuple of the names of the cells.

A cell is a reference to a function's local variables that is used when the function is created by a closure. For example, when you write:
<code>def foo():
    x = 10
    def bar():
        print(x)
    return bar
</code>
The local variable <code>x</code> is a cell in <code>bar</code>'s namespace, as <code>bar</code> has access to it even when <code>foo</code> has returned. This

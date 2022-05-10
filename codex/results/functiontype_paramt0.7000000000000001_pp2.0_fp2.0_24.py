from types import FunctionType
list(FunctionType(lambda x: x*x, globals(), 'f')()) # TypeError: f() missing 1 required positional argument: 'x'
</code>
Why the exception? Why is it not the same as in case of <code>lambda</code>?


A:

<code>lambda</code> is not a function, it's a syntactic sugar for creating <code>FunctionType</code> instances.
In other words, <code>lambda x: x*x</code> is just a shorter way of writing <code>FunctionType(lambda x: x*x, globals(), 'f')</code> (not the best example, I know, but it gets the point across).
That's why it works when you use <code>lambda</code>, and doesn't when you use <code>FunctionType</code> directly.


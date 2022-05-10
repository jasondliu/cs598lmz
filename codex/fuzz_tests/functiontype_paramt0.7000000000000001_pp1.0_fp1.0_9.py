from types import FunctionType
list(FunctionType(lambda: None, globals(), 'my_func'))
</code>
What's going on here?
As mentioned in the documentation, "If <code>iter(p)</code> is implemented, calling it will usually return the iterator object itself."
That's exactly what's happening here. The <code>__iter__</code> method of <code>FunctionType</code> returns the function itself, and you get a list of the function repeated.


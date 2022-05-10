from types import FunctionType
list(FunctionType(x).__code__.co_varnames for x in (y for y in x for x in gc.get_objects() if isinstance(y, type(lambda: None)) or type(y) is FunctionType))
</code>
This gives me something that looks like <code>('&lt;locals&gt;', 'x')</code>
Unfortunately, I have no way of accessing the <code>&lt;locals&gt;</code> object - it's a C object defined in <code>frameobject.c</code> which is internal to CPython. Is there any way to grab a list of local variables that is possibly even slower?


A:

You can get function argument names using <code>inspect.getargspec</code>, but the list of local variables is never available to the program itself. 


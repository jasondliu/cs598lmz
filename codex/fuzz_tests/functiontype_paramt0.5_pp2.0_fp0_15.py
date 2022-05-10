from types import FunctionType
list(FunctionType(code, globals(), 'f'))
</code>
But this doesn't work in Python 2.6, because <code>FunctionType</code> doesn't accept <code>code</code> objects.
I also tried this:
<code>def f():
    yield 1
    yield 2

import inspect
code = inspect.getsource(f).strip()
exec code in globals(), locals()
</code>
But this doesn't work for functions that are defined in another module.
Is there any way to do this?


A:

<code>FunctionType</code> was actually removed in Python 3.0.  In Python 3.2, it was replaced by the <code>types.new_function</code> function.
In Python 2.6, you can use <code>types.FunctionType</code> to create a new function object.  You can then use the <code>inspect</code> module to get the functions code object.  You can then use the <code>types.CodeType</code> constructor to create a new code object.  You can then use the <code>types.FunctionType</

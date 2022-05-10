from types import FunctionType
list(FunctionType(filter(lambda x: x is not None, [None, lambda: None])))
</code>
<code>list(FunctionType(filter(lambda x: x is not None, [None, lambda: None])))
TypeError: 'filter' object is not callable
</code>
I know that <code>filter</code> is a builtin function and I can't override it, but I can't understand why it not callable in this case.


A:

<code>filter</code> is an iterator; you need to consume it.
<code>FunctionType</code> is expecting an iterable, but it does not consume it. Instead, it tries to get the first element of the iterable by calling <code>next(iterable)</code>, which is what raises the exception.
You can consume the iterator by wrapping it in <code>list</code> or <code>tuple</code>:
<code>FunctionType(tuple(filter(lambda x: x is not None, [None, lambda: None])))
</code>


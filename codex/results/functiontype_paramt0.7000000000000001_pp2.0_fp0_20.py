from types import FunctionType
list(FunctionType(code, globals) for code in (
    (lambda x: x),
    (lambda x: x**2),
    (lambda x: x**3),
    (lambda x: x**4),
))
</code>
But it's easier to just use a dict.


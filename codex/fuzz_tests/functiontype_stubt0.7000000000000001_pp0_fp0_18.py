from types import FunctionType
a = (x for x in [1])
b = a.send(2)  # TypeError: 'generator' object is not callable
</code>


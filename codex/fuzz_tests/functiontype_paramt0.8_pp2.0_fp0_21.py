from types import FunctionType
list(FunctionType(f, globals()).__closure__)

</code>
This doesn't work in Python 2, though.


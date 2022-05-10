from types import FunctionType
list(FunctionType(int.__add__, 1).__globals__.values())[0]

# Or:
from operator import methodcaller
methodcaller('__add__', 1).__func__.__globals__[list(methodcaller('__add__', 1).__func__.__globals__)[0]]
</code>


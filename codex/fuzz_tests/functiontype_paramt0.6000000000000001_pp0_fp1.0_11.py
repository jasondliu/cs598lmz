from types import FunctionType
list(FunctionType(lambda: None, globals(), 'f').__code__.co_varnames)

# Python 3.3+
from inspect import signature
signature(lambda: None).parameters

# Python 3.5+
from inspect import signature
signature(lambda: None).parameters.keys()
</code>


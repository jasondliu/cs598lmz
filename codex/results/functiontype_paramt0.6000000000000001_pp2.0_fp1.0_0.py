from types import FunctionType
list(FunctionType(lambda: None, {}).__code__.co_varnames)
import inspect
inspect.getargspec(lambda: None).args
</code>


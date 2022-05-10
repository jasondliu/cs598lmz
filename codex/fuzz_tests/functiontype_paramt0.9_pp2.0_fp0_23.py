from types import FunctionType
list(FunctionType(function.__code__.co_consts[14], globals(), 'foo')())
</code>


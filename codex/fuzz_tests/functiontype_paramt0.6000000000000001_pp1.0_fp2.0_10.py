from types import FunctionType
list(FunctionType(lambda x: x, {}).__code__.co_varnames)
</code>
If you want to get a list of all local variables that are assigned to a value in a scope, you'll have to use the ast module.


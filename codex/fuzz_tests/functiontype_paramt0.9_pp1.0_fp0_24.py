from types import FunctionType
list(FunctionType(foo).__code__.co_varnames)

#['foo', 'bar']
</code>
Credits to Sven Marnach for removing the <code>eval</code> call.


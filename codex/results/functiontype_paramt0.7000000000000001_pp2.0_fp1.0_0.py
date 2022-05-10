from types import FunctionType
list(FunctionType(lambda a: a, {}).__code__.co_freevars)

# [a]
</code>
You can also retrieve the values associated with these names using <code>inspect.getclosurevars</code> (but this will only work for functions created by <code>inspect.getsource</code>):
<code>from types import FunctionType
from inspect import getclosurevars

func = FunctionType(lambda a: a, {})
closure_vars = getclosurevars(func)
print(closure_vars.globals)
# {}
print(closure_vars.nonlocals)
# {}
print(closure_vars.builtins)
# {}
print(closure_vars.unbound)
# {'a': &lt;cell at 0x7f1854bae2b8: int object at 0x7f1855e3f9e0&gt;}
</code>


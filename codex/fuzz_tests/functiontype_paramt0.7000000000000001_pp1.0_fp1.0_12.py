from types import FunctionType
list(FunctionType(lambda x:x,globals()).__code__.co_consts)

# or, when the function f is already available:
list(f.__code__.co_consts)

# or, when the function f is in a module mod:
list(mod.f.__code__.co_consts)
</code>


gi = (i for i in ())
# Test gi.gi_code.co_flags
print(gi.gi_code.co_flags & inspect.CO_GENERATOR)
print(gi.gi_code.co_flags & inspect.CO_ITERABLE_COROUTINE)

co = (lambda: (yield))()
# Test co.gi_code.co_flags
print(co.gi_code.co_flags & inspect.CO_GENERATOR)
print(co.gi_code.co_flags & inspect.CO_ITERABLE_COROUTINE)

co = (lambda: (yield from ()))()
# Test co.gi_code.co_flags
print(co.gi_code.co_flags & inspect.CO_GENERATOR)
print(co.gi_code.co_flags & inspect.CO_ITERABLE_COROUTINE)

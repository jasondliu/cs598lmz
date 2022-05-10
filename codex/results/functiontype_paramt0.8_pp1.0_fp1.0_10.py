from types import FunctionType
list(FunctionType(docstring=None)().__code__.co_consts)

# ['__doc__', '__qualname__', None, None]


print('========================================')
print('============= CO_COROUTINE =============')
print('========================================')


print('============ CO_ITERABLE_COROUTINE ============')

def coroutine1():
    yield
    yield
    yield

import inspect
inspect.isgenerator(coroutine1())
# True
inspect.iscoroutine(coroutine1())
# False
inspect.isawaitable(coroutine1())
# False

list(FunctionType(coroutine1.__code__).__code__.co_flags)
# [<CO_NEWLOCALS: 0>, <CO_OPTIMIZED: 1>, <CO_GENERATOR: 32>]

list(FunctionType(coroutine1.__code__).__code__.co_consts)
# ['__qualname__', None]


print('============= CO_FUTURE_COROUTINE =============')

async def

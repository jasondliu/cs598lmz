from types import FunctionType
list(FunctionType(f.__code__, f.__globals__, 'foo', f.__defaults__, f.__closure__))

# %%
from types import MappingProxyType
d = {1: 'A'}
d_proxy = MappingProxyType(d)
d_proxy
d_proxy[1]
d_proxy[2] = 'x'

# %%
d[2] = 'B'
d_proxy

# %%
from types import SimpleNamespace
data = SimpleNamespace(name='John', age=42)
data.name
data.age

# %%
from types import get_type_hints
def foo(a: int, b: float) -> str:
    return str(a) + str(b)
get_type_hints(foo)

# %%
from types import coroutine
async def my_gen():
    yield 'something'
gen = my_gen()
type(gen)
gen = coroutine(my_gen())
type(gen)

# %%
from types import AsyncGeneratorType
type(

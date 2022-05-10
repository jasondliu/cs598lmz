from types import FunctionType
list(FunctionType(lambda x:x, globals(), 'foo'))

# CodeType
from types import CodeType
CodeType(0, globals(), (), (), '', '', 1, b'', (), (), ())

# MappingProxyType
from types import MappingProxyType
MappingProxyType({})

# SimpleNamespace
from types import SimpleNamespace
SimpleNamespace()

# DynamicClassAttribute
from types import DynamicClassAttribute
DynamicClassAttribute()

# coroutine
from types import coroutine
@coroutine
def foo():
    yield

# AsyncGeneratorType
from types import AsyncGeneratorType
AsyncGeneratorType(iter([]))

# AsyncIterable
from types import AsyncIterable
AsyncIterable()

# AsyncIterator
from types import AsyncIterator
AsyncIterator()

# Awaitable
from types import Awaitable
Awaitable()

# Coroutine
from types import Coroutine
Coroutine()

# GeneratorType
from types import GeneratorType
GeneratorType(iter([]))

# TracebackType
from types import Traceback

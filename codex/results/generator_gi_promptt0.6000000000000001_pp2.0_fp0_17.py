gi = (i for i in ())
# Test gi.gi_code.co_flags & CO_GENERATOR_ALLOWED
def f():
    yield
    yield 1
    yield 2

# Test gi.gi_code.co_flags & CO_COROUTINE
async def f():
    return 42

# Test gi.gi_code.co_flags & CO_ASYNC_GENERATOR
async def f():
    yield
    yield 1
    yield 2

# Test gi.gi_code.co_flags & CO_ITERABLE_COROUTINE
async def f():
    yield 42

# Test gi.gi_code.co_flags & CO_FUTURE_DIVISION
from __future__ import division

# Test gi.gi_code.co_flags & CO_FUTURE_ABSOLUTE_IMPORT
from __future__ import absolute_import

# Test gi.gi_code.co_flags & CO_FUTURE_WITH_STATEMENT
from __future__ import with_statement

# Test gi.gi_code.co_flags & CO_FUTURE

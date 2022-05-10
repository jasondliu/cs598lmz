import types
types.coroutine = types.coroutine

from types import coroutine

from inspect import isawaitable, iscoroutine
from time import sleep
from functools import wraps

from async_generator import async_generator, yield_


@async_generator
async def async_generator_block(value):
    yield value
    await asyncio.sleep(0)



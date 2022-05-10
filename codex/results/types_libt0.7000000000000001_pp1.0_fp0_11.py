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


async def coroutine_block(value):
    yield from value
    await asyncio.sleep(0)


@async_generator
async def async_generator_unblock(value):
    yield value


async def coroutine_unblock(value):
    yield from value


async def nothing():
    pass


async def coroutine_return(value):
    return value


async def coroutine_raise(exc):
    raise exc


def function_return(value):
    return value


def function_raise(exc):
    raise exc


class TestAsyncGenerator(unittest.TestCase):
    def test_async_generator(self

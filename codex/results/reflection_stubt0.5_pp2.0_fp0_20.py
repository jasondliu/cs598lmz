fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__code__.co_filename = '<>'
fn.__code__.co_firstlineno = 1
fn()

# Issue #17483: Ensure that gc.get_referrers() does not raise a
# RecursionError for coroutine objects.
import gc
def g():
    yield
gc.get_referrers(g())

# Issue #17483: Ensure that gc.get_referrers() does not raise a
# RecursionError for generator objects.
def f():
    yield
gc.get_referrers(f())

# Issue #17483: Ensure that gc.get_referrers() does not raise a
# RecursionError for task objects.
import asyncio
async def f():
    await asyncio.sleep(0)
asyncio.run(f())
gc.get_referrers(f())

# Issue #17483: Ensure that gc.get_referrers() does not raise a
# RecursionError for frame objects.
def f():
    return None

import select
# Test select.select at all
select.select([], [], [])
select.select([], [], [], 1.1)

import asyncio
# Test asyncio.run
async def test_run():
    pass
asyncio.run(test_run())
asyncio.run(test_run(), debug=True)

# Test asyncio.run_coroutine_threadsafe
async def test_run_coroutine_threadsafe():
    pass
asyncio.run_coroutine_threadsafe(test_run_coroutine_threadsafe(), loop=None)
asyncio.run_coroutine_threadsafe(test_run_coroutine_threadsafe(), loop=asyncio.get_event_loop())

# Test asyncio.create_task
async def test_create_task():
    pass
asyncio.create_task(test_create_task())

import atexit
# Test atexit.register
def test_register_one():
    pass
atexit.register(test_register_one)
def test_register_two():
    pass
def test

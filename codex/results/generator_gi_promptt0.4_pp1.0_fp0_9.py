gi = (i for i in ())
# Test gi.gi_code
gi.gi_code
# Test gi.gi_frame
gi.gi_frame
# Test gi.gi_running
gi.gi_running
# Test gi.gi_yieldfrom
gi.gi_yieldfrom
# Test gi.send
gi.send(None)
# Test gi.throw
gi.throw(StopIteration)
# Test gi.close
gi.close()
# Test gi.__next__
gi.__next__()

# Test StopIteration
StopIteration
StopIteration.args
StopIteration.with_traceback(None)

# Test StopAsyncIteration
StopAsyncIteration
StopAsyncIteration.args
StopAsyncIteration.with_traceback(None)

# Test coroutine
async def coro():
    await coro
    return
# Test coro.__await__
coro.__await__()
# Test coro.cr_await
coro.cr_await
# Test coro.cr_frame
coro.cr_frame
# Test coro.

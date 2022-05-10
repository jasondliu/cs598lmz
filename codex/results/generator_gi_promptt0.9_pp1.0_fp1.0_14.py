gi = (i for i in ())
# Test gi.gi_code = None
gi = gen_exception()
# Test gi.gi_frame
gi = (i for i in ())
# gi.gi_frame = None
gi = gen_exception()
# Test gi.gi_running
gi = (i for i in ())
# gi.gi_running = None
gi = gen_exception()
# Test gi.gi_yieldfrom
gi = (i for i in ())
# gi.gi_yieldfrom = None
gi = gen_exception()
# Test gi.send()
ex = gen_exception()
next(ex)
# Test gi.throw()
next(gen_exception())
# Test gi.close()
next(gen_exception())

# test coroutine objects
async def coro():
    yield
    return 7

# Test co_name
@NoException
def fn(co):
    assert co.__name__ == 'coro'

m = types.ModuleType('async', doc='async')
m.coro = coro
fn(cor

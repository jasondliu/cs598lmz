gi = (i for i in ())
# Test gi.gi_code is None
print(gi.gi_code)
# Test gi.gi_frame is None
print(gi.gi_frame)

def test(etype, value, tb):
    print("In test", etype, value)
    if etype == StopAsyncIteration:
        print("Normal exit")
    else:
        print("Exception exit")
        # Simulate asynchronous exception
        #set_asyncgen_hook(None)
        #raise value.with_traceback(tb) from None
        raise value

set_asyncgen_hook(test)

async def agen(x):
    yield 1

try:
    g = agen(10)
    g.send(None)
    g.send(None)
    assert False
except Exception as e:
    print("Exception:", e)
    assert isinstance(e, StopAsyncIteration)
else:
    assert False

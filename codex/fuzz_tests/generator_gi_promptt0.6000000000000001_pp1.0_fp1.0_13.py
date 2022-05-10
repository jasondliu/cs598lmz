gi = (i for i in ())
# Test gi.gi_code
# Test gi.gi_frame
# Test gi.gi_running
# Test gi.gi_yieldfrom
# Test gi.__name__
# Test gi.__qualname__
# Test gi.__module__
# Test gi.__dict__
# Test gi.__annotations__
# Test gi.__kwdefaults__
# Test gi.__closure__
# Test gi.__code__
# Test gi.__defaults__
# Test gi.__globals__
# Test gi.__dict__
# Test gi.__weakref__
# Test gi.send
# Test gi.throw
# Test gi.close
# Test gi.__next__
# Test gi.send
# Test gi.throw
# Test gi.close


# fmt: off
def gi2():
    yield
    yield
gi2 = (i for i in ())
# fmt: on
# Test gi2.gi_code
# Test gi2.gi_frame
# Test gi2

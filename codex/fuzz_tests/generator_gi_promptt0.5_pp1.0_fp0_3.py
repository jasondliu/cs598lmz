gi = (i for i in ())
# Test gi.gi_code
# Test gi.gi_frame
# Test gi.gi_running
# Test gi.gi_yieldfrom
gi.gi_frame = None
gi.gi_running = False
gi.gi_yieldfrom = None
# Test gi.__next__
# Test gi.close
# Test gi.send
# Test gi.throw
# Test gi.__del__
del gi

# Test types.CodeType
# Test types.FrameType
# Test types.TracebackType
# Test types.GeneratorType

# Test inspect.isgenerator
# Test inspect.isgeneratorfunction

# Test StopIteration.with_traceback

# Test PEP 380: yield from

def gen():
    yield from range(3)

# Test gen.gi_frame
# Test gen.gi_running
# Test gen.gi_yieldfrom
# Test gen.__next__
# Test gen.send
# Test gen.throw
# Test gen.close
# Test gen.__del__
del gen

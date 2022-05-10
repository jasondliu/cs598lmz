gi = (i for i in ())
# Test gi.gi_code:
expectError(TypeError, setattr, gi, 'gi_code', None)
expectError(TypeError, setattr, gi, 'gi_code', gen_finds_stop)
# Test gi.gi_frame
expectError(TypeError, setattr, gi, 'gi_frame', None)
# Test gi.gi_running
expectError(TypeError, setattr, gi, 'gi_running', None)
expectError(TypeError, setattr, gi, 'gi_running', False)
try:
    gi.__next__()
except StopIteration:
    pass
expectError(ValueError, setattr, gi, 'gi_running', 1)

# Test GeneratorExit exception handling
def gen_with_yield_from():
    yield from [1]
    yield
    yield from gen_throws()
    yield  # Never reached

def gen_throws():
    try:
        yield
    except GeneratorExit:
        pass
    raise GeneratorExit

def gen_exit_handled():


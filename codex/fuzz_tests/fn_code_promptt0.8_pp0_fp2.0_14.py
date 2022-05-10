fn = lambda: None
# Test fn.__code__.co_filename
def test_co_filename():
    assert fn.__code__.co_filename == 'pyro_test.py'

# Test fn.__code__.co_firstlineno
def test_co_firstlineno():
    assert fn.__code__.co_firstlineno == 42   # hmmm...

# Test fn.__code__.co_flags
def test_co_flags():
    assert fn.__code__.co_flags == 0

# Test sys.settrace()
def test_settrace():

    def tracer(frame, event, arg):
        return tracer
    
    sys.settrace(tracer)
    assert sys.gettrace() == tracer
    sys.settrace(None)
    assert sys.gettrace() == None

# Test sys.setprofile()
def test_setprofile():

    def profiler(frame, event, arg):
        return profiler
    
    sys.setprofile(profiler)
    assert sys.getprofile() == profiler
    sys.setprofile(None)


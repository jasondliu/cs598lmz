gi = (i for i in ())
# Test gi.gi_code is None
gi.gi_code

# Test sys.setprofile()
def profiler(frame, event, arg):
    global profiler_test_result
    profiler_test_result = (event, frame.f_code.co_filename)
    return profiler

sys.setprofile(profiler)

def foo():
    pass

def bar():
    foo()

sys.setprofile(None)

bar()
assert profiler_test_result == ("call", __file__)

# Test sys.settrace()
def tracer(frame, event, arg):
    global tracer_test_result
    tracer_test_result = (event, frame.f_code.co_filename)
    return tracer

sys.settrace(tracer)

def foo():
    pass

def bar():
    foo()

sys.settrace(None)

bar()
assert tracer_test_result == ("call", __file__)

# Test sys.settrace() when it returns None
def tracer(frame, event, arg

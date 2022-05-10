gi = (i for i in ())
# Test gi.gi_code is not None
expectException(TypeError, gi.gi_code.__get__, gi)
# Test gi.gi_frame is None
expectException(TypeError, gi.gi_frame.__get__, gi)
# Test gi.gi_running is False
expectException(TypeError, gi.gi_running.__get__, gi)
# Test gi.gi_yieldfrom is None
expectException(TypeError, gi.gi_yieldfrom.__get__, gi)

# Test gi.gi_code is not None
def f():
    yield
gi = f()
expectException(AttributeError, gi.__setattr__, 'gi_code', None)

# Test gi.gi_frame is None
gi = f()
expectException(AttributeError, gi.__setattr__, 'gi_frame', None)

# Test gi.gi_running is False
gi = f()
expectException(AttributeError, gi.__setattr__, 'gi_running', False

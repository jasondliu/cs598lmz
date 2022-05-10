gi = (i for i in ())
# Test gi.gi_code
try:
    gi.gi_code
except AttributeError:
    pass
else:
    print('FAILED: generator.gi_code')

# Test gi.gi_frame
try:
    gi.gi_frame
except AttributeError:
    pass
else:
    print('FAILED: generator.gi_frame')

# Test gi.gi_running
try:
    gi.gi_running
except AttributeError:
    pass
else:
    print('FAILED: generator.gi_running')

# Test gi.gi_yieldfrom
try:
    gi.gi_yieldfrom
except AttributeError:
    pass
else:
    print('FAILED: generator.gi_yieldfrom')

# Test gi.send
try:
    gi.send(None)
except TypeError:
    pass
else:
    print('FAILED: generator.send')

# Test gi.throw
try:
    gi.throw(StopIteration)
except StopIteration:

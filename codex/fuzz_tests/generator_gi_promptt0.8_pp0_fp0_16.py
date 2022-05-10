gi = (i for i in ())
# Test gi.gi_code
print gi.gi_code
# Test gi.gi_frame
print gi.gi_frame
# Test gi.gi_running
print gi.gi_running
# Test gi.gi_yieldfrom
print gi.gi_yieldfrom

a = float(1)
# Test type(a).__class__
print type(a).__class__
# Test type(a).__bases__
print type(a).__bases__
# Test type(a).__mro__
print type(a).__mro__
# Test type(a).__name__
print type(a).__name__
# Test type(a).__dict__
print type(a).__dict__

# Test type(a).__doc__
print type(a).__doc__

# Test type(a).__module__
print type(a).__module__

# Test type(a).__call__
print type(a).__call__

# Test type(a).__getattr__
_ = type(a).__getattr__




gi = (i for i in ())
# Test gi.gi_code
print gi.gi_code
# Assign to gi.gi_code
gi.gi_code = lambda: None

# Now get ready for a sequence of methods
# that should raise AttributeError when
# called on a built-in method
for meth in ('gi_running', 'gi_frame', 'gi_yieldfrom',
    'gi_name', 'gi_qualname', 'gi_exc_state',
    'gi_exc_traceback', 'gi_exc_type', 'gi_exc_value'):
    try:
        getattr(gi, meth)
    except AttributeError:
        print meth, "not found"
# As a side effect, this should have
# raised a TypeError

# The following should all raise TypeError
try:
    gi.gi_frame = None
except TypeError:
    print "Assignment to gi_frame"
try:
    gi.gi_code = object()
except TypeError:
    print "Assignment to gi_code"
try:
    gi.gi_running = True
except

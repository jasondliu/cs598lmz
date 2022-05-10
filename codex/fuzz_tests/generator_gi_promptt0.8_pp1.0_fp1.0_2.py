gi = (i for i in ())
# Test gi.gi_code is None

# Test __reduce__ doesn't break things
import pickle
print(pickle.loads(pickle.dumps(gi)))

for name in dir(gi):
    exec("%s = gi.%s" % (name, name), globals())

gi.gi_code = selfref
print(gi.gi_code is selfref)

# Test gi.gi_code.co_code
print(gi.gi_code.co_code)
gi.gi_code.co_code = None

# Test gi_frame
gi.gi_frame = selfref
print(gi.gi_frame is selfref)

gi.gi_frame = None
gi.gi_frame = object()
print(gi.gi_frame)

# Test gi_running
print(gi.gi_running)
gi.gi_running = selfref
print(gi.gi_running is selfref)

# Test gi_yieldfrom

# Test tp_iternext
try:
    next(gi)
except StopIteration:


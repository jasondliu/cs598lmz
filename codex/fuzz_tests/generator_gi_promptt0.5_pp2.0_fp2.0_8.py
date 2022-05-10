gi = (i for i in ())
# Test gi.gi_code is None.

gi = (i for i in ())
gi.gi_code = None
# Test gi.gi_frame is None.

gi = (i for i in ())
gi.gi_frame = None
# Test gi.gi_running is False.

gi = (i for i in ())
gi.gi_running = False
# Test gi.gi_yieldfrom is None.

gi = (i for i in ())
gi.gi_yieldfrom = None
# Test gi.send() raises TypeError.

gi = (i for i in ())
try:
    gi.send(None)
except TypeError:
    pass
else:
    print('TypeError expected')
# Test gi.throw() raises TypeError.

gi = (i for i in ())
try:
    gi.throw(None)
except TypeError:
    pass
else:
    print('TypeError expected')
# Test gi.close() raises TypeError.

gi = (i for i in ())
try:
    gi.close()
except

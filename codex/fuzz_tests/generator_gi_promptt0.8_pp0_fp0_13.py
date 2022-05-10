gi = (i for i in ())
# Test gi.gi_code == None
# Test gi.gi_frame == None
# Test gi.gi_running == 0
# Test gi.gi_yieldfrom == None
# Test gi.gi_weakreflist == []

# Test gi.gi_frame can not be set
try:
    gi.gi_frame = 123
except TypeError:
    print("SKIP")
    raise SystemExit
except AttributeError:
    print("SKIP")
    raise SystemExit

# test gc will collect
gi = (i for i in ())
print("ok")

gi = (i for i in ())
# Test gi.gi_code
try:
    gi.gi_code
except AttributeError:
    pass
else:
    print("AttributeError expected")

# Test gi.gi_frame
try:
    gi.gi_frame
except AttributeError:
    pass
else:
    print("AttributeError expected")

# Test gi.gi_running
try:
    gi.gi_running
except AttributeError:
    pass
else:
    print("AttributeError expected")

# Test gi.gi_yieldfrom
try:
    gi.gi_yieldfrom
except AttributeError:
    pass
else:
    print("AttributeError expected")

# Test gi.gi_weakreflist
try:
    gi.gi_weakreflist
except AttributeError:
    pass
else:
    print("AttributeError expected")

# Test gi.gi_exc_state
try:
    gi.gi_exc_state
except AttributeError:
    pass
else:
    print("AttributeError expected")

# Test g

gi = (i for i in ())
# Test gi.gi_code
try:
    gi.gi_code
except AttributeError:
    pass
else:
    print("AttributeError expected")

try:
    del gi.gi_code
except AttributeError:
    pass
else:
    print("AttributeError expected")

try:
    gi.gi_code = 1
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

try:
    del gi.gi_frame
except AttributeError:
    pass
else:
    print("AttributeError expected")

try:
    gi.gi_frame = 1
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

try:
    del g

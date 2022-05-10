gi = (i for i in ())
# Test gi.gi_code
try:
    gi.gi_code
except AttributeError:
    print("AttributeError")
else:
    print("no AttributeError")
# Test gi.gi_frame
try:
    gi.gi_frame
except AttributeError:
    print("AttributeError")
else:
    print("no AttributeError")
# Test gi.gi_running
try:
    gi.gi_running
except AttributeError:
    print("AttributeError")
else:
    print("no AttributeError")
# Test gi.gi_yieldfrom
try:
    gi.gi_yieldfrom
except AttributeError:
    print("AttributeError")
else:
    print("no AttributeError")
# Test gi.gi_name
try:
    gi.gi_name
except AttributeError:
    print("AttributeError")
else:
    print("no AttributeError")
# Test gi.gi_qualname
try:
    gi.gi_qualname
except AttributeError:
    print("AttributeError")

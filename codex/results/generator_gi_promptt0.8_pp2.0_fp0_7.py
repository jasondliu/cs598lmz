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
# Test gi.send(123)
try:
    gi.send(123)
except TypeError:
    pass
else:
    print("TypeError expected")
# Test gi.send(None)
try:
    gi.send(None)
except TypeError:
    pass
else:
    print("TypeError expected")
# Test gi.throw(StopIteration)
try:
    g

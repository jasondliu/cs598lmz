gi = (i for i in ())
# Test gi.gi_code
gi.gi_code
try:
    gi.gi_code = None
except TypeError:
    print("TypeError")
# Test gi.gi_frame
#    gi.gi_frame #<don't care>
# Test gi.gi_running
#    gi.gi_running #<don't care>
# Test gi.gi_yieldfrom
#    gi.gi_yieldfrom #<don't care>
# Test gi.__name__
try:
    gi.__name__ = None
except TypeError:
    print("TypeError")
# Test gi.__module__
try:
    gi.__module__ = None
except TypeError:
    print("TypeError")
# Test gi.__qualname__
try:
    gi.__qualname__ = None
except TypeError:
    print("TypeError")
# Test gi.__annotations__
gi.__annotations__
try:
    gi.__annotations__ = None
except TypeError:
    print("TypeError")


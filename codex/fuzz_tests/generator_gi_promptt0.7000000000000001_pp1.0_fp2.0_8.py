gi = (i for i in ())
# Test gi.gi_code is None.
# gi.gi_frame is None.
# gi.gi_running is False.
# gi.gi_yieldfrom is None.
# gi.send(None) raises TypeError.
try:
    gi.send(None)
except TypeError:
    print("OK")
else:
    print("NO")
# gi.throw(StopIteration) raises StopIteration.
try:
    gi.throw(StopIteration)
except StopIteration:
    print("OK")
else:
    print("NO")
# gi.close() raises StopIteration.
try:
    gi.close()
except StopIteration:
    print("OK")
else:
    print("NO")

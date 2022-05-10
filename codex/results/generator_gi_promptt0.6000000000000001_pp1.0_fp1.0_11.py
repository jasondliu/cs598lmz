gi = (i for i in ())
# Test gi.gi_code
print("gi.gi_code: ", gi.gi_code)
# Test gi.gi_frame
print("gi.gi_frame: ", gi.gi_frame)
# Test gi.gi_running
print("gi.gi_running: ", gi.gi_running)
# Test gi.gi_yieldfrom
print("gi.gi_yieldfrom: ", gi.gi_yieldfrom)

# Test gi.__next__
try:
    gi.__next__()
except StopIteration:
    print("gi.__next__: ", "StopIteration")

# Test gi.send
try:
    gi.send(None)
except StopIteration:
    print("gi.send(None): ", "StopIteration")

# Test gi.throw
try:
    gi.throw(StopIteration)
except StopIteration:
    print("gi.throw(StopIteration): ", "StopIteration")

# Test gi.close
gi.close()

# Test gi.gi_

gi = (i for i in ())
# Test gi.gi_code is None
print(gi.gi_code)
# Test gi.gi_frame is None
print(gi.gi_frame)
# Test gi.gi_running is False
print(gi.gi_running)
# Test gi.gi_yieldfrom is None
print(gi.gi_yieldfrom)

# Test gi.send(None)
print(gi.send(None))

# Test gi.send(1)
try:
    gi.send(1)
except StopIteration as e:
    print(e.value)

# Test gi.throw(TypeError)
try:
    gi.throw(TypeError)
except TypeError:
    print("TypeError")

# Test gi.close()
gi.close()

# Test gi.send(None)
try:
    gi.send(None)
except StopIteration:
    print("StopIteration")

# Test gi.throw(TypeError)
try:
    gi.throw(TypeError)
except StopIteration:
   

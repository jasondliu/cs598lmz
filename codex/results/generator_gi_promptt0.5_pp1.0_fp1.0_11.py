gi = (i for i in ())
# Test gi.gi_code
print(type(gi.gi_code))
print(type(gi.gi_frame))
print(type(gi.gi_running))
print(type(gi.gi_yieldfrom))

# Test gi.send
print(gi.send(None))
try:
    print(gi.send(None))
except StopIteration:
    print("Caught StopIteration")
try:
    print(gi.send(None))
except StopIteration:
    print("Caught StopIteration")

# Test gi.throw
try:
    gi.throw(ValueError)
except ValueError:
    print("Caught ValueError")
try:
    print(gi.send(None))
except StopIteration:
    print("Caught StopIteration")

# Test gi.close
gi.close()
try:
    print(gi.send(None))
except StopIteration:
    print("Caught StopIteration")

# Test gi.__next__
try:
    print(gi.__next__())
except StopIteration

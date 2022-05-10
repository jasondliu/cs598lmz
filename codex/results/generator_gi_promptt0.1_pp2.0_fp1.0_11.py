gi = (i for i in ())
# Test gi.gi_code
print(gi.gi_code)
# Test gi.gi_frame
print(gi.gi_frame)
# Test gi.gi_running
print(gi.gi_running)
# Test gi.gi_yieldfrom
print(gi.gi_yieldfrom)

# Test gi.send
print(gi.send(None))
# Test gi.throw
try:
    gi.throw(Exception)
except Exception:
    print("Exception")
# Test gi.close
gi.close()
# Test gi.gi_frame
print(gi.gi_frame)

# Test gi.send
try:
    gi.send(None)
except StopIteration:
    print("StopIteration")

# Test gi.throw
try:
    gi.throw(Exception)
except StopIteration:
    print("StopIteration")

# Test gi.close
gi.close()

# Test gi.gi_frame
print(gi.gi_frame)

# Test gi.send
try:


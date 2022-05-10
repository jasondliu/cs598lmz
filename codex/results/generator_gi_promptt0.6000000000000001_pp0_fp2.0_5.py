gi = (i for i in ())
# Test gi.gi_code
print(gi.gi_code)
# Test gi.gi_frame
print(gi.gi_frame)
# Test gi.gi_running
print(gi.gi_running)
# Test gi.gi_yieldfrom
print(gi.gi_yieldfrom)
# Test gi.gi_yieldfrom.__name__
print(gi.gi_yieldfrom.__name__)
# Test gi.gi_yieldfrom.__qualname__
print(gi.gi_yieldfrom.__qualname__)

# Test gi.send
try:
    gi.send(None)
except StopIteration:
    print('gi.send(None) StopIteration')
try:
    gi.send(None)
except StopIteration:
    print('gi.send(None) StopIteration')

# Test gi.throw
try:
    gi.throw(Exception)
except Exception:
    print('gi.throw(Exception) Exception')

# Test gi.close
gi.close()
try:
   

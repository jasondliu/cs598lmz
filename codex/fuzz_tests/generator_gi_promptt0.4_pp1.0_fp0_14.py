gi = (i for i in ())
# Test gi.gi_code
print(gi.gi_code)
# Test gi.gi_frame
print(gi.gi_frame)
# Test gi.gi_running
print(gi.gi_running)
# Test gi.gi_yieldfrom
print(gi.gi_yieldfrom)
# Test gi.send(None)
print(gi.send(None))
# Test gi.throw(StopIteration)
print(gi.throw(StopIteration))
# Test gi.close()
print(gi.close())

# Test gi.send(None)
try:
    print(gi.send(None))
except StopIteration:
    print('StopIteration')

# Test gi.throw(StopIteration)
try:
    print(gi.throw(StopIteration))
except StopIteration:
    print('StopIteration')

# Test gi.close()
try:
    print(gi.close())
except StopIteration:
    print('StopIteration')

# Test gi.gi_code
print(gi.gi_

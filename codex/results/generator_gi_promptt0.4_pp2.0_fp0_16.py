gi = (i for i in ())
# Test gi.gi_code
print(gi.gi_code)
# Test gi.gi_frame
print(gi.gi_frame)
# Test gi.gi_running
print(gi.gi_running)
# Test gi.gi_yieldfrom
print(gi.gi_yieldfrom)

# Test gi.send(value)
print(gi.send(None))
# Test gi.send(value)
try:
    print(gi.send(None))
except StopIteration:
    print('StopIteration')
# Test gi.send(value)
try:
    print(gi.send(None))
except StopIteration:
    print('StopIteration')

# Test gi.throw(type)
try:
    print(gi.throw(TypeError))
except TypeError:
    print('TypeError')
# Test gi.throw(type)
try:
    print(gi.throw(TypeError))
except TypeError:
    print('TypeError')
# Test gi.throw(type)
try:
    print(gi.throw(

gi = (i for i in ())
# Test gi.gi_code
print(gi.gi_code)
# Test gi.gi_frame
print(gi.gi_frame)
# Test gi.gi_running
print(gi.gi_running)
# Test gi.gi_yieldfrom
print(gi.gi_yieldfrom)

# Test next(gi)
try:
    next(gi)
except StopIteration:
    print('StopIteration')

# Test gi.send(None)
try:
    gi.send(None)
except StopIteration:
    print('StopIteration')

# Test gi.throw(TypeError)
try:
    gi.throw(TypeError)
except StopIteration:
    print('StopIteration')
except TypeError:
    print('TypeError')

# Test gi.close()
gi.close()

# Test gi.send(None)
try:
    gi.send(None)
except StopIteration:
    print('StopIteration')
except RuntimeError:
    print('RuntimeError')

# Test gi

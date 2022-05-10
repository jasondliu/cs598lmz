gi = (i for i in ())
# Test gi.gi_code
print(gi.gi_code.co_name)
# Test gi.gi_frame
print(gi.gi_frame)
# Test gi.gi_running
print(gi.gi_running)
# Test gi.__name__
print(gi.__name__)
# Test gi.__qualname__
print(gi.__qualname__)
# Test gi.send
try:
    print(gi.send(None))
except StopIteration:
    print('StopIteration')
# Test gi.throw
try:
    print(gi.throw(TypeError))
except TypeError:
    print('TypeError')
except StopIteration:
    print('StopIteration')
# Test gi.close
gi.close()
try:
    print(gi.send(None))
except StopIteration:
    print('StopIteration')
try:
    print(gi.throw(TypeError))
except TypeError:
    print('TypeError')
except StopIteration:
    print('StopIteration')

# Test __next__


gi = (i for i in ())
# Test gi.gi_code
print(gi.gi_code)
# Test gi.gi_frame
print(gi.gi_frame)
# Test gi.gi_running
print(gi.gi_running)
# Test gi.gi_yieldfrom
print(gi.gi_yieldfrom)

# Test gi.__name__
print(gi.__name__)
# Test gi.__qualname__
print(gi.__qualname__)

# Test gi.send
try:
    gi.send(1)
except StopIteration as e:
    print(e)

# Test gi.throw
try:
    gi.throw(TypeError)
except TypeError:
    print('TypeError')

# Test gi.close
gi.close()

# Test gi.gi_frame.f_lasti
print(gi.gi_frame.f_lasti)
# Test gi.gi_frame.f_lineno
print(gi.gi_frame.f_lineno)
# Test gi.gi_frame.f_

gi = (i for i in ())
# Test gi.gi_code and gi.gi_frame
print('gi:', gi.gi_code is empty_code, gi.gi_frame is empty_frame)

# Make an iterator
def func(n):
    yield from range(n, 0, -1)
c = func(3)
# Test c.gi_code and c.gi_frame
print('c:', c.gi_code is f_code, c.gi_frame is start_frame)

# Now call func()
next(c)
# Test c.gi_code and c.gi_frame
print('c:', c.gi_code is f_code, c.gi_frame is start_frame)

# Now yield a value
next(c)
# Test c.gi_code and c.gi_frame
print('c:', c.gi_code is empty_code, c.gi_frame is empty_frame)

# Now we are done
next(c)
# Test c.gi_code and c.gi_frame
print('c:', c.gi_code is empty_code, c.

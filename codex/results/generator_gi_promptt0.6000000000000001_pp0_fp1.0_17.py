gi = (i for i in ())
# Test gi.gi_code is None.
print(gi.gi_code)

# Test gi.gi_frame is None.
print(gi.gi_frame)

# Test gi.gi_running
print(gi.gi_running)

# Test gi.gi_yieldfrom
print(gi.gi_yieldfrom)

# Test gi.__next__()
print(next(gi))

# Test gi.send(val)
print(gi.send(1))

# Test gi.throw(type, val, tb)
print(gi.throw(Exception, Exception('exception'), 'tb'))

# Test gi.close()
print(gi.close())

# Test gi.gi_frame.clear()
print(gi.gi_frame.clear())

# Test gi.gi_frame.f_back
print(gi.gi_frame.f_back)

# Test gi.gi_frame.f_builtins
print(gi.gi_frame.f_builtins)

# Test gi.gi_frame

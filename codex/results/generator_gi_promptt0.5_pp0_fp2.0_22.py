gi = (i for i in ())
# Test gi.gi_code
print(gi.gi_code.co_name)
print(gi.gi_code.co_filename)
print(gi.gi_code.co_firstlineno)

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
    gi.throw(TypeError)
    print(False)
except TypeError:
    print(True)

# Test gi.close
gi.close()

# Test gi.gi_frame.f_back
print(gi.gi_frame.f_back)

# Test gi.gi_frame.f_builtins
print(gi.gi_frame.f_builtins)

# Test gi.gi_frame.f_code
print(gi.gi_frame.f_code)



gi = (i for i in ())
# Test gi.gi_code.co_filename
print(gi.gi_code.co_filename)
# Test gi.gi_code.co_name
print(gi.gi_code.co_name)
# Test gi.gi_frame.f_lineno
print(gi.gi_frame.f_lineno)
# Test gi.gi_frame.f_locals
print(gi.gi_frame.f_locals)
# Test gi.gi_frame.f_trace
print(gi.gi_frame.f_trace)

# Test gi.gi_running
print(gi.gi_running)
# Test gi.__next__
print(gi.__next__())
# Test gi.send
print(gi.send(None))

# Test gi.throw
try:
    gi.throw(ZeroDivisionError)
except ZeroDivisionError as e:
    pass

# Test gi.close
try:
    gi.close()
except StopIteration as e:
    pass

# Test gi.gi_frame.f_

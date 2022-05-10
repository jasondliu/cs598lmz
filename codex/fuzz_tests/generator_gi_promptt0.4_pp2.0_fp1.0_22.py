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
# Test gi.__module__
print(gi.__module__)
# Test gi.__next__
print(gi.__next__())
# Test gi.send
# print(gi.send(None))
# Test gi.throw
# print(gi.throw(StopIteration))
# Test gi.close
# print(gi.close())

# Test gi.gi_frame.f_code.co_name
print(gi.gi_frame.f_code.co_name)
# Test gi.gi_frame.f_code.co_filename
print(gi.gi_frame.f_

gi = (i for i in ())
# Test gi.gi_code
print(gi.gi_code)
# Test gi.gi_frame
print(gi.gi_frame)
# Test gi.gi_running
print(gi.gi_running)
# Test gi.gi_yieldfrom
print(gi.gi_yieldfrom)
# Test gi.send()
print(gi.send(None))
# Test gi.throw()
print(gi.throw(StopIteration))
# Test gi.close()
print(gi.close())
# Test gi.send() after gi.close()
try:
    print(gi.send(None))
except StopIteration:
    print("StopIteration")
# Test gi.throw() after gi.close()
try:
    print(gi.throw(StopIteration))
except StopIteration:
    print("StopIteration")

# Test gi_frame.f_back
print(gi.gi_frame.f_back)
# Test gi_frame.f_builtins
print(gi.gi_frame.f_builtins)
#

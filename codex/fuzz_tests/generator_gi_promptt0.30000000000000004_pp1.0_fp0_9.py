gi = (i for i in ())
# Test gi.gi_code
print(gi.gi_code)
# Test gi.gi_frame
print(gi.gi_frame)
# Test gi.gi_running
print(gi.gi_running)
# Test gi.gi_yieldfrom
print(gi.gi_yieldfrom)
# Test gi.send
print(gi.send(None))
# Test gi.throw
print(gi.throw(StopIteration))
# Test gi.close
print(gi.close())

# Test generator expression
ge = (i for i in ())
# Test ge.gi_code
print(ge.gi_code)
# Test ge.gi_frame
print(ge.gi_frame)
# Test ge.gi_running
print(ge.gi_running)
# Test ge.gi_yieldfrom
print(ge.gi_yieldfrom)
# Test ge.send
print(ge.send(None))
# Test ge.throw
print(ge.throw(StopIteration))
# Test ge.close
print(ge.close())

# Test async generator
as

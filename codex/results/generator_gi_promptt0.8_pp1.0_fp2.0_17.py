gi = (i for i in ())
# Test gi.gi_code
print(gi.gi_code)
# Test gi.gi_frame
print(gi.gi_frame)
# Test gi.gi_running
print(gi.gi_running)
# Test gi.send
print(gi.send(None))
# Test gi.throw
print(gi.throw(StopIteration))
# Test gi.close
print(gi.close())
# Test gi.gi_yieldfrom
print(gi.gi_yieldfrom)
# Test gi.gi_yieldfrom.send
print(gi.gi_yieldfrom.send(None))
# Test gi.gi_yieldfrom.throw
print(gi.gi_yieldfrom.throw(StopIteration))
# Test gi.gi_yieldfrom.close
print(gi.gi_yieldfrom.close())

def f():
    yield
gi = f()
# Test gi.gi_code
print(gi.gi_code)
# Test gi.gi_frame
print(gi.gi_frame)
# Test gi.gi

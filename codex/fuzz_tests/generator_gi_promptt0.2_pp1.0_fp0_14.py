gi = (i for i in ())
# Test gi.gi_code is None
print(gi.gi_code)
# Test gi.gi_frame is None
print(gi.gi_frame)
# Test gi.gi_running is False
print(gi.gi_running)
# Test gi.gi_yieldfrom is None
print(gi.gi_yieldfrom)

# Test gi.send(None)
print(gi.send(None))
# Test gi.send(1)
print(gi.send(1))

# Test gi.throw(Exception)
try:
    gi.throw(Exception)
except Exception:
    print("Exception")
# Test gi.throw(Exception, Exception("test"))
try:
    gi.throw(Exception, Exception("test"))
except Exception as e:
    print(e)
# Test gi.throw(Exception, "test")
try:
    gi.throw(Exception, "test")
except Exception as e:
    print(e)
# Test gi.throw(Exception, None)
try:
    gi.throw(Exception, None)

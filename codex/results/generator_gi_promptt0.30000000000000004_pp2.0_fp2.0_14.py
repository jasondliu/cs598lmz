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

# Test gi.throw(None)
print(gi.throw(None))

# Test gi.close()
gi.close()

# Test gi.send(None)
print(gi.send(None))

# Test gi.throw(None)
print(gi.throw(None))

# Test gi.close()
gi.close()

# Test gi.send(None)
print(gi.send(None))

# Test gi.throw(None)
print(gi.throw(None))

# Test gi.close()
gi.close()

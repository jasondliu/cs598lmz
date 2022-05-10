gi = (i for i in ())
# Test gi.gi_code
print(gi.gi_code)
# Test gi.gi_frame
print(gi.gi_frame)
# Test gi.gi_running
print(gi.gi_running)
# Test gi.gi_yieldfrom
print(gi.gi_yieldfrom)

# Test gi.send(None)
print(gi.send(None))
# Test gi.send(1)
print(gi.send(1))
# Test gi.throw(TypeError)
print(gi.throw(TypeError))
# Test gi.throw(TypeError, 1)
print(gi.throw(TypeError, 1))
# Test gi.throw(TypeError, 1, 2)
print(gi.throw(TypeError, 1, 2))
# Test gi.close()
print(gi.close())

# Test gi.send(None)
print(gi.send(None))
# Test gi.send(1)
print(gi.send(1))
# Test gi.throw(TypeError)
print(gi.throw(TypeError

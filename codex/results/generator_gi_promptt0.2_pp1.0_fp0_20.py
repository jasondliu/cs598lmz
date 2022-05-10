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
# Test gi.send(2)
print(gi.send(2))
# Test gi.send(3)
print(gi.send(3))
# Test gi.send(4)
print(gi.send(4))
# Test gi.send(5)
print(gi.send(5))
# Test gi.send(6)
print(gi.send(6))
# Test gi.send(7)
print(gi.send(7))
# Test gi.send(8)
print(gi.send(8))
# Test gi.send(

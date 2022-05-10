gi = (i for i in ())
# Test gi.gi_code is None
print(gi.gi_code)
# Test gi.gi_frame is None
print(gi.gi_frame)
# Test gi.gi_running is False
print(gi.gi_running)
# Test gi.gi_yieldfrom is None
print(gi.gi_yieldfrom)

# Test gi.send(<throw>) will raise TypeError
# gi.send(42)
# Test gi.throw(<throw>) will raise TypeError
# gi.throw(RuntimeError, 'error')
# Test gi.close() will raise TypeError
# gi.close()

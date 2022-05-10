gi = (i for i in ())
# Test gi.gi_code and gi.gi_frame
print gi.gi_code
print gi.gi_frame

# Test gi.send()
gi.send(1)  # TypeError: can't send non-None value to a just-started generator

# Test gi.throw()
gi.throw(TypeError, 'test')  # StopIteration

# Test gi.close()
gi.close()  # RuntimeError: generator ignored GeneratorExit

# Test gi.next()
gi.next()  # StopIteration

# Test gi.gi_running
print gi.gi_running  # False

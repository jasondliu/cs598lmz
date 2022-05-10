gi = (i for i in ())
# Test gi.gi_code
gi.gi_code
# Test gi.gi_frame
gi.gi_frame
# Test gi.gi_running
gi.gi_running
# Test gi.next()
gi.next()
# Test gi.send(3)
gi.send(3)
# Test gi.throw(TypeError)
gi.throw(TypeError)
# Test gi.throw(TypeError, 3)
gi.throw(TypeError, 3)
# Test gi.throw(TypeError, 3, 4)
gi.throw(TypeError, 3, 4)

# Test generator expressions
gi = (i for i in range(1))
gi = (i for i in range(1) for j in range(2))
gi = (i for i in range(1) if i)
gi = (i for i in range(1) if i if i % 2)

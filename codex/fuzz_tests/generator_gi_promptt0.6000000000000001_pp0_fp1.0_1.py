gi = (i for i in ())
# Test gi.gi_code
gi.gi_code
# Test gi.gi_frame
gi.gi_frame
# Test gi.gi_name
gi.gi_name
# Test gi.gi_running
gi.gi_running
# Test gi.gi_yieldfrom
gi.gi_yieldfrom
# Test gi.send
gi.send(None)
# Test gi.throw
gi.throw(GeneratorExit)
# Test gi.close
gi.close()
# Test gi.send
gi.send(None)

# Test generator with send, next, throw, close
def g():
    yield 1
    yield 2
    yield 3

# Test g.gi_code
g.gi_code
# Test g.gi_frame
g.gi_frame
# Test g.gi_name
g.gi_name
# Test g.gi_running
g.gi_running
# Test g.gi_yieldfrom
g.gi_yieldfrom

# Test g.send
g.send(None)
# Test g.next
g.next()

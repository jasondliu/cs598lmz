gi = (i for i in ())
# Test gi.gi_code
gi.gi_code
# Test gi.gi_frame
gi.gi_frame
# Test gi.gi_running
gi.gi_running
# Test gi.gi_yieldfrom
gi.gi_yieldfrom
# Test gi.send
gi.send(None)
# Test gi.throw
gi.throw(StopIteration)
# Test gi.close
gi.close()
# Test gi.__next__
gi.__next__()
# Test gi.send
gi.send(None)
# Test gi.throw
gi.throw(StopIteration)
# Test gi.close
gi.close()

# Test generator.gi_code
def gen():
    yield 1
gen().gi_code
# Test generator.gi_frame
def gen():
    yield 1
gen().gi_frame
# Test generator.gi_running
def gen():
    yield 1
gen().gi_running
# Test generator.gi_yieldfrom
def gen():
    yield 1
gen().gi_yieldfrom
# Test generator.send


gi = (i for i in ())
# Test gi.gi_code
gi.gi_code.co_varnames
gi.gi_code.co_filename
gi.gi_code.co_name
gi.gi_closure
gi.gi_frame
gi.gi_running
gi.gi_yieldfrom
# Test gi.gi_weakreflist
wrl = gi.gi_weakreflist
# Test wrl.data
for x in wrl.data:
    pass
# Test wrl.last
wrl.last

# Test generators
def foo():
    yield

gi = foo()
# Test gi.gi_code
gi.gi_code.co_varnames
gi.gi_code.co_filename
gi.gi_code.co_name
gi.gi_closure
gi.gi_frame
gi.gi_running
gi.gi_yieldfrom
# Test gi.gi_weakreflist
wrl = gi.gi_weakreflist
# Test wrl.data
for x in wrl.data:
    pass
# Test wrl.last
wrl.last

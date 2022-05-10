fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
try:
    fn()
except TypeError:
    pass
else:
    raise Exception("should not be able to call function with generator code")

# test that generator can be pickled
import pickle
pickle.loads(pickle.dumps(gi))

# test that generator can be deepcopied
import copy
copy.deepcopy(gi)

# test that generator can be marshalled
import marshal
marshal.loads(marshal.dumps(gi))

# test generator type
if type(gi) != type(gi.gi_code):
    raise Exception("type(gi) is %r" % type(gi))

# test generator code type
if type(gi.gi_code) != type(gi.gi_frame):
    raise Exception("type(gi.gi_code) is %r" % type(gi.gi_code))

# test generator frame type

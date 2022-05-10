fn = lambda: None
gi = (i for i in ())
fn.__code__ = 'foo'
gi.gi_code = 'foo'

# Verify that the code object that is created is a string.
s = pickle.dumps(fn)
assert isinstance(pickle.loads(s).__code__, str)
s = pickle.dumps(gi)
assert isinstance(pickle.loads(s).gi_code, str)

# Verify that a code object with a module attribute that is a string pickles
# and unpickles correctly.
s = pickle.dumps(fn.__code__)
assert pickle.loads(s) is fn.__code__
s = pickle.dumps(gi.gi_code)
assert pickle.loads(s) is gi.gi_code

# Verify that a code object with a module attribute that is a unicode string
# pickles and unpickles correctly.
fn.__code__.co_filename = u'foo'
gi.gi_code.co_filename = u'foo'
s = pickle.dumps(fn.__code__)
assert pickle.loads(s)

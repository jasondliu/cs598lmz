gi = (i for i in ())
# Test gi.gi_code.co_name
assert gi.gi_code.co_name == '<genexpr>'

def g():
    a = yield
    yield a

# Test g.gi_code.co_name
assert g.gi_code.co_name == 'g'

s = ''.join(('a', 'b', 'c'))
# Test s.__class__.__name__
assert s.__class__.__name__ == 'str'

# Test s.__class__.__bases__
bases = (object,)
assert s.__class__.__bases__ == bases

# Test s.__class__.__mro__ == (str, object)
assert s.__class__.__mro__ == (str, object)

# Test s.__class__.__bases__[0] == object
assert s.__class__.__bases__[0] == object

# Test s.__class__.__name__ == 'str'
assert s.__class__.__name__ == 'str'

print "

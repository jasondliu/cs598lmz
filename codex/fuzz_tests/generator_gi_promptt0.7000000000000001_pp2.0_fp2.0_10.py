gi = (i for i in ())
# Test gi.gi_code would raise AttributeError.
try:
    gi.gi_code
except AttributeError:
    pass
else:
    print("FAILED: gi.gi_code didn't raise AttributeError")

# gc_refs
#

try:
    import _testcapi
except ImportError:
    import sys
    print("SKIP")
    sys.exit()

def callback(x):
    global y
    return y

def gc_refs():
    # Check that gc_refs() returns a list of all the objects with a
    # reference to the object passed in
    global y
    y = callback
    refs = gc.get_referents(callback)
    # We should get a list of 3 objects:
    #  - y
    #  - the function object
    #  - the code object
    assert len(refs) == 3
    assert callback in refs
    assert gc.get_referents(callback) == refs


gc_refs()

# Issue #22355: check

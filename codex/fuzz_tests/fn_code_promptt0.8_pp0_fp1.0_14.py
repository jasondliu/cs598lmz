fn = lambda: None
# Test fn.__code__
testfn.__code__ = sys.getcode(testfn)

# Sanity check: testfn() should fail with a NameError
try:
    testfn()
except NameError:
    pass

# Now patch testfn.__code__.co_names
testfn.__code__ = sys.replace_code_object(testfn, testfn.__code__,
                                          {'co_names': ('spam', 'eggs')})

# Now testfn() succeeds
testfn()

# Sanity check: testfn2() should also succeed
testfn2()

# Now undo the effect by setting co_names to its original value
testfn.__code__ = sys.replace_code_object(testfn, testfn.__code__,
                                          {'co_names': orig_names})

# testfn() and testfn2() should fail again
try:
    testfn()
except NameError:
    pass
try:
    testfn2()
except NameError:
    pass

# Test the optional 'names' argument
testfn

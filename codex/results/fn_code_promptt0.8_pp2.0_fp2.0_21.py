fn = lambda: None
# Test fn.__code__.co_varnames.
# Should return (None, <should-be-tuple>) or (<C-tuple>, <Python-tuple>)
TestError(r"""fn = lambda: None
try:
    fn.__code__.co_varnames
except AttributeError:
    print(None, tuple())
else:
    print(tuple(fn.__code__.co_varnames), tuple(["text"]))
""", "None, ()", sort=False)

# Test fn.__code__.co_flags.
# Should return (None, <should-be-int>) or (<C-int>, <Python-int>)
TestError(r"""fn = lambda: None
try:
    fn.__code__.co_flags
except AttributeError:
    print(None, 0)
else:
    print(fn.__code__.co_flags, 0)
""", "None, 0", sort=False)

# Test fn.__code__.co_lnotab.
# Should return (None, <should-be-bytes>)

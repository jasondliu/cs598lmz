fn = lambda: None
# Test fn.__code__ is None.
assert fn.__code__ is None
# Test fn.__closure__ is None.
assert fn.__closure__ is None
# Test fn.__defaults__ is None.
assert fn.__defaults__ is None
# Test fn.__get__ is None.
assert fn.__get__ is None
# Test fn.__kwdefaults__ is None.
assert fn.__kwdefaults__ is None
# Test fn.__name__ is None.
assert fn.__name__ is None
# Test fn.__objclass__ is None.
assert fn.__objclass__ is None
# Test fn.__self__ is None.
assert fn.__self__ is None
# Test fn.__text_signature__ is None.
assert fn.__text_signature__ is None
# Test fn.__globals__ is {}.
assert fn.__globals__ == {}
# Test fn.__dict__ is {}.
assert fn.__dict__ == {}


# @dolang.typed(a=int)
def fn1(a):
    return

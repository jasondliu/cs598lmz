gi = (i for i in ())
# Test gi.gi_code == <code object <genexpr> at 0x...>
# We could check for the code type attribute gi_frame
# (i.e. gi.gi_code.__code__.co_flags & CO_GENERATOR_ALLOWED), but it
# introduces a dependency on CPython's internal structures.
assert gi.gi_code.co_name == '<genexpr>'


def f():
    yield


try:
    f.__code__ = 'not a real code object'
except TypeError:
    pass
else:
    assert False, "should've failed to set __code__ to 'not a real code object'"


class Code:
    pass


try:
    f.__code__ = Code()
except TypeError:
    pass
else:
    assert False, "should've failed to set __code__ with a custom object"


# Issue #16517: when calling a code object, do not enforce co_flags
# other than CO_VARARGS, CO_VARKEYWORDS, CO_NESTED, CO_GENERATOR,

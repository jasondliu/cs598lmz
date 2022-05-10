fn = lambda: None
# Test fn.__code__.co_argcount

# co_varnames
# co_flags
def test_1(a, *args, b, c=1, d=2, e, **kwargs):
    """ fn's code
    """
    pass

test_1.__code__.co_varnames
test_1.__code__.co_argcount
test_1.__code__.co_flags

test_1.__code__.co_filename
test_1.__code__.co_name
test_1.__code__.co_firstlineno
test_1.__code__.co_lnotab
test_1.__code__.co_consts
test_1.__code__.co_names
test_1.__code__.co_varnames
test_1.__code__.co_stacksize
test_1.__code__.co_code
test_1.__code__.co_lnotab
# From Python 3.3, code objects have a co_posonlyargcount attribute

# cf. __code

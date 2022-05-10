gi = (i for i in ())
# Test gi.gi_code is a code_wrapper
def test_gi_has_co_code():
    print(gi.gi_code.co_code)

# Test gi.gi_code.co_code is read-only
def test_gi_co_code_readonly():
    try:
        gi.gi_code.co_code = b'a'
    except AttributeError:
        print('co_code read-only')
    else:
        raise AssertionError('co_code not read-only')

# Test gi.gi_code is writable
def test_gi_code_writable():
    code = gi.gi_code
    # Replace generator iterator code with a new code
    # using the existing code as the basis.
    # Should not segfault, and the new code should then be
    # the one visible in gi.gi_code.
    gi.gi_code = types.CodeType(
        code.co_argcount, code.co_kwonlyargcount, code.co_nlocals,
        code.co_st

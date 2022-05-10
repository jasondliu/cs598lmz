import codecs

def add_one_codepoint(exc):
    return ("a", exc.start)

def add_utf16_bytes(exc):
    return (b'ab', exc.start)

def add_utf32_bytes(exc):
    return (b'abcd', exc.start)

codecs.register_error("add_one_codepoint", add_one_codepoint)
codecs.register_error("add_utf16_bytes", add_utf16_bytes)
codecs.register_error("add_utf32_bytes", add_utf32_bytes)

def test_main(verbose=None):
    from test import test_support
    from test import string_tests
    tests = [string_tests]
    test_support.run_unittest(*tests)

    # verify reference counting
    if verbose and hasattr(sys, "gettotalrefcount"):
        import gc
        counts = [None] * 5
        for i in range(len(counts)):
            test_support.run_unittest(*tests)
            gc.collect()
            counts[i] = sys.gettotalrefcount()
        print(counts)

def test_main2():
    # verify exception arguments are not affected
    # XXX - could be moved to a separate test file
    try:
        raise ValueError('one\rtwo')
    except ValueError as e:
        if e.args == ('one\rtwo',):
            raise
        else:
            print('ValueError did not propagate arguments correctly')
    else:
        print('ValueError was not raised')

    # verify that errors raised from the wrapped


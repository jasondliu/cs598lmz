import codecs
# Test codecs.register_error
#
def test_main():
    #
    # test codecs.register_error
    #
    # In the first test, we check that a custom error handler is indeed
    # used.  The custom handler replaces "ab" with "abab"
    #
    from test import test_support
    import codecs
    import StringIO
    import sys

    def replace_with_ab(exc):
        if isinstance(exc, UnicodeEncodeError):
            s = []
            for c in exc.object[exc.start:exc.end]:
                s.append(c)
                s.append(c)
            return (u"".join(s), exc.end)
        elif isinstance(exc, UnicodeDecodeError):
            return (u"".join([u"a", u"b"] * (exc.end - exc.start)), exc.end)
        else:
            raise TypeError("don't know how to handle %r" % exc)

    codecs.register_error("test.replace_with_ab", replace_with_ab)

    # test

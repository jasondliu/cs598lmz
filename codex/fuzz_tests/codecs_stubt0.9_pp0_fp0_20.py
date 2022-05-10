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

encoding = "utf-32"
encoding = "utf-16"
encoding = "utf-8"

def repl_func(exc):
    if not isinstance(exc, UnicodeEncodeError):
        raise TypeError("don't know how to handle %r" % exc)

    if len(exc.object) == 6:
        # error at end of string
        raise

    return (u"A", exc.start+1)       # blah blah blah

codecs.register_error("test.where", repl_func)

def show_exception(exception):
    print("%-27s %10s %s" % (
        exception.__class__.__name__,
        exception.encoding,
        exception.object[exception.start:exception.end]))
    print("    %s" % exception.reason)

# UnicodeEncodeError

s = "\x9b\x3c\xca\x80"
s = "\x79\x80"
s = "\xf9\x9b\x3c\

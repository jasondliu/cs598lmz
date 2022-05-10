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

def print_eol(eol):
    print("'%s' %r" % (eol, eol))
    print("%s:'%s' %r" % (eol, eol, eol))
    print("'%s:%s' %r" % (eol, eol, eol))
    print("'%s\n' %r" % (eol, eol))
    print("'\n%s' %r" % (eol, eol))
    print("'\n%s\n' %r" % (eol, eol))
    print("'" + eol + "' %r" % eol)
    print("'" + eol + "':'%s' %r" % (eol, eol))
    print("'" + eol + "':'" + eol + "' %r" % eol)
    print("'" + eol + "\n' %r" % eol)
    print("'\n" + eol + "' %r" % eol)
    print("'

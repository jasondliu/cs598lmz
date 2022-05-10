import codecs
# Test codecs.register_error()

# It was wrong before unicodedata was imported.
# J.F. Sebastian reported that it worked after the import.

def bad():
    try:
        u"\ufffe".encode("utf-8")
    except UnicodeEncodeError:
        pass
    else:
        raise TestFailed("did not raise UnicodeEncodeError")

def good():
    try:
        u"\ufffe".encode("utf-8")
    except UnicodeEncodeError:
        raise TestFailed("shouldn't raise UnicodeEncodeError")

good()
codecs.register_error("test.ignore", lambda e: (u'\ufffd',e.end))
bad()
good()
codecs.register_error("test.ignore", None)
bad()

# Test codecs.escape_encode()

def test_escape_encode():
    s = "test"
    l = []
    codecs.escape_encode(s, l.append)
    if ''.join(l) != (r"\x74\x65

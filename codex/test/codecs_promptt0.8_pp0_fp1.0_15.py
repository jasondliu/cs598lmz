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

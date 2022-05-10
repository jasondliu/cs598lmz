import codecs
# Test codecs.register_error

def my_replace(exc):
    if isinstance(exc, UnicodeDecodeError):
        return (u'', exc.end)
    else:
        raise TypeError("don't know how to handle %r" % exc)

# replace
codecs.register_error("test.replace", my_replace)

for encoding in ["ascii", "latin-1", "utf-8"]:
    print encoding,
    try:
        print codecs.decode("\xff", encoding, "test.replace")
    except UnicodeDecodeError:
        print "UnicodeDecodeError"

# ignore
codecs.register_error("test.ignore", codecs.ignore_errors)

for encoding in ["ascii", "latin-1", "utf-8"]:
    print encoding,
    try:
        print codecs.decode("\xff", encoding, "test.ignore")
    except UnicodeDecodeError:
        print "UnicodeDecodeError"

# xmlcharrefreplace
codecs.register_error("test

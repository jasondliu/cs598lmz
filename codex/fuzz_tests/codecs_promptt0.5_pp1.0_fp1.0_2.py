import codecs
# Test codecs.register_error('strict', codecs.strict_errors)

# This is used in the error handler for the 'replace' mode
# to insert U+FFFD into the Unicode stream.

# The 'xmlcharrefreplace' error handler is used by the
# xmlcharrefreplace codec.

def xmlcharrefreplace_errors(exc):
    if isinstance(exc, (UnicodeEncodeError, UnicodeTranslateError)):
        res = []
        for c in exc.object[exc.start:exc.end]:
            res.append(u'&#%d;' % ord(c))
        return (u''.join(res), exc.end)
    else:
        raise TypeError("don't know how to handle %r" % exc)

codecs.register_error('xmlcharrefreplace', xmlcharrefreplace_errors)

# The 'backslashreplace' error handler is used by the
# backslashreplace codec.

def backslashreplace_errors(exc):
    if isinstance(exc, (UnicodeEncodeError, UnicodeTranslateError)

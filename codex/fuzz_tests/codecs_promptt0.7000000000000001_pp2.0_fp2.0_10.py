import codecs
# Test codecs.register_error('replace_with_space', my_replace_with_space)
#
# See http://stackoverflow.com/questions/13590795/
#   python-unicodedecodeerror-ascii-codec-cant-decode-byte-0xe2-in-position

def my_replace_with_space(exc):
    """Used to replace (some) UnicodeDecodeErrors with spaces."""
    if not isinstance(exc, (UnicodeDecodeError, UnicodeEncodeError)):
        raise TypeError("Expected UnicodeDecodeError or UnicodeEncodeError, "
                        "got %r" % exc)
    return (u' ', exc.start + 1)

codecs.register_error('replace_with_space', my_replace_with_space)

def u(s):
    return unicode(s, 'utf8', errors='replace_with_space')

def uu(s):
    return unicode(s, 'utf8', errors='replace')


class InvenioWebSearchUnknownCollectionError(Exception):


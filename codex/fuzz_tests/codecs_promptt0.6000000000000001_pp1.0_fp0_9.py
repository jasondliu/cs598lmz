import codecs
# Test codecs.register_error

# --------------------------------------------------------------------

import codecs

def hex_escape(exc):
    if isinstance(exc, (UnicodeEncodeError, UnicodeDecodeError)):
        s = [ ('\\x' + hex(ord(c))[2:].zfill(2)) for c in exc.object[exc.start:exc.end] ]
        return (''.join(s), exc.end)
    else:
        # call back to the original exception handler
        return codecs.xmlcharrefreplace_errors(exc)

codecs.register_error('hex', hex_escape)

# --------------------------------------------------------------------

import codecs

def hex_escape(exc):
    if isinstance(exc, (UnicodeEncodeError, UnicodeDecodeError)):
        s = [ ('\\x' + hex(ord(c))[2:].zfill(2)) for c in exc.object[exc.start:exc.end] ]
        return (''.join(s), exc.end)
    else:
        # call back to the original exception handler
        return codecs.

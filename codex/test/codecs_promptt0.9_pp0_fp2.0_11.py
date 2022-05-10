import codecs
# Test codecs.register_error with an error that takes a unicode
# argument and returns a string, and with an error that just takes
# a string argument and return a string.  Not much testing
# actually happens here, because utf_8_replace and the ones that
# follow it just die on their input anyway.

def utf_8_replace(u, exc):
    if isinstance(exc, UnicodeEncodeError):
        if isinstance(u, unicode):
            return u.encode('latin-1')
        else:
            return exc.object[exc.start].encode('latin-1')
    else:
        u, start, end = exc.object[exc.start:exc.end], 0, len(u)
        for i in range(len(u)):
            if (ord(u[i]) & 0xff80) != 0:
                u = u[:i] + u[i].encode('latin-1', 'replace') + u[i+1:]
        return u


import codecs
# Test codecs.register_error

import codecs

class E(Exception):
    pass

def register_error(encoding):
    def xmlcharrefreplace(exc):
        if isinstance(exc, UnicodeEncodeError):
            s = [u'&#%d;' % ord(exc.object[idx]) for idx in range(exc.start, exc.end)]
            return (u''.join(s), exc.end)
        else:
            raise E("don't know how to handle %r" % exc)
    codecs.register_error(encoding, xmlcharrefreplace)

register_error('xmlcharrefreplace')
register_error('backslashreplace')

# test UnicodeEncodeError
for obj in (u'\u1234', 'xx\u1234xx', u'\u1234\u5678'):
    for errors in ('strict', 'ignore', 'replace', 'xmlcharrefreplace', 'backslashreplace'):
        print '%r, %s: ' % (obj, errors),
        try:
            s = obj.encode

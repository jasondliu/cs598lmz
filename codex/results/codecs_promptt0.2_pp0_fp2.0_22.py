import codecs
# Test codecs.register_error()

import codecs

def my_replace(exc):
    if isinstance(exc, UnicodeDecodeError):
        return (u'', exc.end)
    else:
        raise TypeError("don't know how to handle %r" % exc)

codecs.register_error('my_replace', my_replace)

print repr(u'\xff'.encode('ascii', 'my_replace'))
print repr(u'\xff'.encode('ascii', 'replace'))
print repr(u'\xff'.encode('ascii', 'ignore'))
print repr(u'\xff'.encode('ascii', 'xmlcharrefreplace'))
print repr(u'\xff'.encode('ascii', 'backslashreplace'))
print repr(u'\xff'.encode('ascii', 'namereplace'))

# Test codecs.register_error()

import codecs

def my_replace(exc):
    if isinstance(exc, UnicodeDecodeError):
        return (u'', exc

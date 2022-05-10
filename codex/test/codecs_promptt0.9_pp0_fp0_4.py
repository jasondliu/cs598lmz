import codecs
# Test codecs.register_error
s = b'\xc3\xa4\xc3\xb6\xc3\xbc\xc3\x84\xc3\x96\xc3\x9c'
a = u"äöüÄÖÜ aabcdefghijklmnopqrstuvwxyz".encode('utf-8')
u1 = "äöüÄÖÜ aabcdefghijklmnopqrstuvwxyz".encode('utf-8').decode('cp1252')
def replace(exc):
    if not isinstance(exc, UnicodeDecodeError):
        raise TypeError("don't know how to handle %r" % exc)
    print('replace(%r): %r' % (exc.args[1], exc.args[2]))
    return ('?', exc.end)
codecs.register_error('replace', replace)
u2 = s.decode('utf-8', 'replace')
print("expect", u1)
print("actual", u2)

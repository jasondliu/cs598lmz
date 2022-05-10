import codecs
# Test codecs.register_error()

import codecs

def raise_exc(exc):
    raise exc

def ignore_exc(exc):
    return u'', exc.end

def xmlcharrefreplace_exc(exc):
    if not isinstance(exc, UnicodeEncodeError):
        raise TypeError("don't know how to handle %r" % exc)
    l = []
    for c in exc.object[exc.start:exc.end]:
        l.append(u'&#%d;' % ord(c))
    return (u''.join(l), exc.end)

for name in ['ignore', 'replace', 'xmlcharrefreplace', 'backslashreplace',
             'namereplace']:
    codecs.register_error(name, globals()[name+'_exc'])

for encoding in ['ascii', 'latin-1', 'utf-8', 'utf-16']:
    print '%s:' % encoding
    for name in ['strict', 'ignore', 'replace', 'xmlcharrefreplace',
                 'backslashreplace', 'name

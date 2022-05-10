import codecs
# Test codecs.register_error()

import sys

def test_register_error():
    # Test codecs.register_error()
    errors = [
        'ignore',
        'replace',
        'xmlcharrefreplace',
        'backslashreplace',
        'namereplace',
        ]
    # test first without registering anything
    for e in errors:
        try:
            "abc".encode("ascii", e)
        except LookupError:
            pass
        else:
            raise TestFailed, "lookup of %s should have failed" % e
    # test with registering
    for e in errors:
        if e == 'ignore':
            codecs.register_error(e, lambda x: (u'', 0))
        elif e == 'replace':
            codecs.register_error(e, lambda x: (u'!', 1))
        elif e == 'xmlcharrefreplace':
            codecs.register_error(e, lambda x: (u'&#%d;' % ord(x.object[x.start]), 1))
        elif e

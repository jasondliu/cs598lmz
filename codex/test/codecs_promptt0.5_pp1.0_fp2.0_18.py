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

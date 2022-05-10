import codecs
# Test codecs.register_error()

def lookuperror():
    return codecs.lookup_error('strict')

import test.test_codecs

def test_register_error():
    errors = [('ignore', None), ('replace', '?'), ('xmlcharrefreplace', None),
              ('strict', test.test_codecs.UnicodeEncodeError),
              ('backslashreplace', None)]
    #
    for e, etype in errors:
        codecs.register_error(e, lookuperror)
        if etype:
            raises(etype, codecs.charmap_encode, 'hello')
        else:
            codecs.charmap_encode('hello', 'strict')
    #
    # unregistering should reset the error handling function to its
    # original value (or to the "strict" error handler)
    for e, etype in errors:
        codecs.register_error(e, None)
        if etype:
            raises(etype, codecs.charmap_encode, 'hello')


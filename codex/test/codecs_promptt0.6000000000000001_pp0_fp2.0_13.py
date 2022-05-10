import codecs
# Test codecs.register_error

import encodings.cp1252

def bad_decode_handler(exception):
    return (u'\ufffd', exception.end)

def bad_encode_handler(exception):
    return (u'\ufffd', exception.end)

def test_register_error():
    # Encoding "cp1252" is unavailable to the encodings package,
    # so we register a handler for it here.
    codecs.register_error('strict', bad_decode_handler)
    codecs.register_error('ignore', None)
    codecs.register_error('replace', bad_encode_handler)
    codecs.register_error('xmlcharrefreplace', None)
    codecs.register_error('backslashreplace', None)

    # Now we can use "cp1252" as an encoding.
    u = u'\u5d14\u6587\u6587'.encode('cp1252').decode('cp1252')

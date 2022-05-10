import codecs
# Test codecs.register_error() with raw unicode codec

import codecs
text = str("\xff\xfe\x00\x01\x00\x02", 'raw-unicode-escape')

def error_handler(exception):
    return ('\ufffd', exception.end)

codecs.register_error('test.rawunicode', error_handler)

utf32be = codecs.getincrementalencoder('utf-32be')()
utf32le = codecs.getincrementalencoder('utf-32le')()
for char in text:
    print(utf32be.encode(char), utf32le.encode(char))

print()

utf32be = codecs.getincrementalencoder('utf-32be', 'test.rawunicode')()
utf32le = codecs.getincrementalencoder('utf-32le', 'test.rawunicode')()
for char in text:
    print(utf32be.encode(char), utf32le.encode(char))

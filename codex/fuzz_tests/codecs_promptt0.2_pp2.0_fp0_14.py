import codecs
# Test codecs.register_error

import codecs

def handler(exception):
    return (u"", exception.end)

codecs.register_error("test.myhandler", handler)

# Test the basic codecs

for encoding in ['base64_codec', 'quopri_codec']:
    print encoding, "->",
    s = unicode("abc123", encoding)
    print repr(s)
    print repr(s.encode(encoding))

# Test the error handler

for encoding in ['base64_codec', 'quopri_codec']:
    print encoding, "->",
    s = unicode("abc123", encoding, "test.myhandler")
    print repr(s)
    print repr(s.encode(encoding))

# Test the incremental encoder

for encoding in ['base64_codec', 'quopri_codec']:
    print encoding, "->",
    s = unicode("abc123", encoding)
    print repr(s)
    print repr(s.encode(encoding))
   

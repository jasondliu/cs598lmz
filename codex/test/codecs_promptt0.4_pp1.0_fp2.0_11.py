import codecs
# Test codecs.register_error

import codecs

def test(codec, input, expected):
    try:
        codecs.lookup_error(codec)
    except LookupError:
        pass

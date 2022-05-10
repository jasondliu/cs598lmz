import codecs

def add_one_codepoint(exc):
    return ("a", exc.start)

def add_utf16_bytes(exc):
    return (b'ab', exc.start)

def add_utf32_bytes(exc):
    return (b'abcd', exc.start)

codecs.register_error("add_one_codepoint", add_one_codepoint)
codecs.register_error("add_utf16_bytes", add_utf16_bytes)
codecs.register_error("add_utf32_bytes", add_utf32_bytes)

def expect_error(msg, codec, s, exc_type):
    try:
        codec.encode(s)
    except exc_type:
        #expected error
        pass
    else:
        print("expected exception from '%s', got none" % msg)

def expect_no_error(msg, codec, s, exc_type):
    try:
        codec.encode(s)
    except exc_type:
        print("expected no exception from '%s' but got out of buffer error" % msg)
    else:
        pass

s = "cafe"

for encoding in ('utf-16-be', 'utf-16-le', 'utf-16'):
    #raising the error is a buffer error
    expect_error("%s strict" % encoding, codecs.getencoder(encoding), s, codecs.BufferError)

    expect_no_error("%s add_utf16_bytes" % encoding, codecs.getencoder(encoding, 'add_utf16_bytes'), s, codecs.BufferError)



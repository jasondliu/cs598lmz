import codecs
# Test codecs.register_error

# dummy error handler
def bad_decode(input, errors="strict"):
    return u"\uff", len(input)

def bad_encode(input, errors="strict"):
    return u"\uff".encode("ascii"), len(input)

codecs.register_error("bad_decode", bad_decode)
codecs.register_error("bad_encode", bad_encode)

# error handler oneshot
print codecs.decode("hello", "ascii", errors="bad_decode")
print codecs.encode(u"hello", "ascii", errors="bad_encode")

# error handler for specific codec
codecs.register(lambda na: (None, None, None, None), "mycodec")
codecs.register_error("myerror", bad_decode)
print codecs.decode("hello", "mycodec", errors="myerror")

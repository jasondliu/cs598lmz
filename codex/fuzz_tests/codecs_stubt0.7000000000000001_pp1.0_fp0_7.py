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

def print_list(list):
    print(list)
    for x in list:
        print(x)
    print()

def print_codec(name, stream=False):
    if stream:
        print(name + " StreamReader:")
        stream_reader = codecs.getreader(name)
        print(stream_reader)
        print()

        print(name + " StreamWriter:")
        stream_writer = codecs.getwriter(name)
        print(stream_writer)
        print()

    print(name + " IncrementalDecoder:")
    incr_dec = codecs.getincrementaldecoder(name)()
    print(incr_dec)
    print()

    print(name + " IncrementalEncoder:")
    incr_enc = codecs.getincrementalencoder(name)()
    print(incr_enc)
    print()

    print(name + " Decoder:")
    dec = codecs.getdecoder(name)
    print(dec)
    print()

    print(name +

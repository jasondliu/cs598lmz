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

def test_main():
    # Test codecs.decode()
    #
    # codecs.decode(input, errors='strict')
    #
    # should raise a UnicodeDecodeError if the input
    # contains undecodable characters
    #
    # codecs.decode(input, errors='ignore')
    #
    # should ignore undecodable characters
    #
    # codecs.decode(input, errors='replace')
    #
    # should replace undecodable characters with the
    # official unicode replacement character U+FFFD
    #
    # codecs.decode(input, errors=callable)
    #
    # should call the callable with a UnicodeDecodeError
    # instance as argument and expect it to return
    # the tuple (replacement, new position)
    #
    # All of these behaviours should be tested for
    # all codecs that support the 'decode' method

    # Test codecs.encode()
    #
    # codecs.encode(input, errors='strict')
   

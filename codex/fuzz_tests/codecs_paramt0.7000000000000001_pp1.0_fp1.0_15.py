import codecs
codecs.register_error('surrogate_or_uncodable', surrogatepass)

# Tests

################
# Decoding Tests#
################

# Test decoding with byte input and a surrogatepass error handler
# (which simply skips the byte)

def test_byte_input_surrogatepass():
    for i in range(0x100):
        assert codecs.utf_16_decode(bytes([i]), 'surrogatepass') == (
            '\udcff' + chr(i), 2)
    assert codecs.utf_16_decode(bytes([0, 0]), 'surrogatepass') == ('\0', 2)
    assert codecs.utf_16_decode(bytes([1, 0]), 'surrogatepass') == ('\1', 2)
    assert codecs.utf_16_decode(bytes([0, 1]), 'surrogatepass') == ('\udcff'
        '\1', 2)


# Test decoding with byte input and a default error handler

def test_byte_input_default():
    for i in range(0x

import bz2
# Test BZ2Decompressor.decompress()

# This is a list of test cases. Each test case is a tuple:
# (input, output, unconsumed_tail, error_indicator)
# input: The input string to decompress()
# output: The expected output from decompress()
# unconsumed_tail: The expected value of the unconsumed_tail attribute
# error_indicator: The expected value of the eof attribute

test_cases = [
    # Test empty string
    (b"", b"", b"", False),
    # Test short string
    (b"BZ", b"", b"BZ", False),
    # Test that we can decompress a whole file
    (bz2.compress(b"foo"), b"foo", b"", False),
    # Test that we can decompress a whole file plus a little bit
    (bz2.compress(b"foo") + b"bar", b"foo", b"bar", False),
    # Test that we can decompress a whole file plus a little bit
    # (with a short input)
    (bz2

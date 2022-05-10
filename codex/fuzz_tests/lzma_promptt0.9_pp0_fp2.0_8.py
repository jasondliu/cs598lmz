import lzma
# Test LZMADecompressor and LZMACompressor functions for the expected exceptions
# when called with illegal arguments

def check_illegal_arguments(name, *args):
    try:
        method(*args)
    except TypeError:
        pass
    except Exception as e:
        raise AssertionError("%s() didn't raise TypeError when passed illegal arguments" % name) from e

fd = lzma.open(TESTFN, mode="w")
fd.close()
fd = open(TESTFN, "rb")

compressor = lzma.LZMACompressor()

# Check illegal arguments
check_illegal_arguments("LZMACompressor.__init__", 2)
check_illegal_arguments("LZMACompressor.flush", "arg")
check_illegal_arguments("LZMACompressor.copy", 2)
check_illegal_arguments("LZMACompressor.copy.__init__", 2)
check_illegal_arguments("LZMACompressor.copy.flush", "arg")

# Test the .copy() method
compressor.compress

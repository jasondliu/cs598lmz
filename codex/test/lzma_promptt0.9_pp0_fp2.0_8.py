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


import codecs
# Test codecs.register_error()
def bad_decode(input, errors='strict'):
    raise UnicodeDecodeError("bad input", input, 0, 1, "bad message")
codecs.register_error("test.bad_decode", bad_decode)
def bad_encode(input, errors='strict'):
    raise UnicodeEncodeError("bad input", input, 0, 1, "bad message")
codecs.register_error("test.bad_encode", bad_encode)
import sys
sys.setrecursionlimit(5000)
# End test codecs.register_error()

def testUTF8():
    # This is a very extensive test for the UTF-8 codec
    # written by Marc-Andre Lemburg (mal@lemburg.com).

    import _codecs_cn, _codecs_hk, _codecs_iso2022, _codecs_jp, _codecs_kr, _codecs_tw, _codecs_kr
    encoding = 'utf-8'
    test_support.verbose = 1
   

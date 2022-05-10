gi = (i for i in ())
# Test gi.gi_code
#
# Test that gi.gi_code.co_code is a bytes
# (It used to be a string but that's not correct)
#
# CPython issue number: 19288
import dis

def test():
    gi = (i for i in ())
    return gi.gi_code

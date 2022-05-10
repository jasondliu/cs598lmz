from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('d', 0)
s.format = s._fmt
S_LONG_SIZE = s.size
S_PTR_SIZE = s.size
del s
def _test():
    import sys, _testcapi

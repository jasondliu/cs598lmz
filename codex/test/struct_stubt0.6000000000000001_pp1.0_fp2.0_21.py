from _struct import Struct
s = Struct.__new__(Struct)
s.format = 'i'
s.size = 4
s.__getattr__(b'format')

def _test():
    import doctest, sys
    return doctest.testmod(sys.modules[__name__])

if __name__ == "__main__":
    _test()

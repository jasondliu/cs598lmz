from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('d', 0)
s.format = s._fmt
S_LONG_SIZE = s.size
S_PTR_SIZE = s.size
del s
def _test():
    import sys, _testcapi
    print 'sys.version                :', sys.version
    print 'sys.hexversion             :', hex(sys.hexversion)
    print 'sys.subversion             :', sys.subversion
    print 'sys.api_version            :', sys.api_version
    print 'string.letters             :', string.letters
    print 'string.ascii_letters       :', string.ascii_letters
    print 'string.digits              :', string.digits
    print 'string.hexdigits           :', string.hexdigits
    print 'string.octdigits           :', string.octdigits
    print 'string.punctuation         :', string.punctuation
    print 'string.printable           :', string.printable
    print 'string.whitespace          :', string.whitespace


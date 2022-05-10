import ctypes

class S(ctypes.Structure):
    x = (ctypes.c_int * 2)()

s = S()
ctypes.cast(ctypes.addressof(s), ctypes.POINTER(ctypes.c_int))

#OK s.x[0]
#OK s.x[-1]
#OK s.x[1]
#OK s.x[2]
#OK s.x[3]

ExpectedTypeError("(-1-sys.maxint-1)", 'IndexError', globs=globals())

ExpectedTypeError("(0-0)", 'IndexError', globs=globals())

ExpectedTypeError("s.x.__getitem__(long(1))", 'OverflowError', globs=globals())

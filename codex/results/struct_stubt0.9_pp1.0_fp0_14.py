from _struct import Struct
s = Struct.__new__(Struct)  
s, s.size, s.pack, s.unpack
s.__init__('10s f')
s.size, s.pack('abc', 3.145), s.unpack(s.pack('abc', 3.145))
isinstance(s.pack('abc', 3.145), bytearray)

# file handling
from _io import open
fp  = open('test.dat', 'wb')
a = np.arange(10000)
a.tofile(fp)
fp.close()
fp  = open('test.dat', 'rb')
b = np.fromfile(fp, dtype='uint32')
fp.close()
b[:10]

# import CPython
import _ctypes
cpp = _ctypes.PyDLL('./cpp.so', mode=_ctypes.RTLD_GLOBAL)
cpp.__name__
p = cpp.test()
p.f
p.f = lambda x: 3*x
p.f(3)
p._dispose_()

# Python's internal C0

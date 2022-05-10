import ctypes
# Test ctypes.CFUNCTYPE.
print ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
# Test ctypes.POINTER.
print ctypes.POINTER(ctypes.c_int)
ctypes.CDLL(None)
# Proposed new format type.
print "%#.32d" % 1
# Test saving floats to binary files...
f = open(r'testfload', 'wb')
f.write(struct.pack('d', float('3.14e9')))
f.write(struct.pack('d', float('-3.14e9')))
f.close()
f = open(r'testfload', 'rb')
print float(f.read(8)), float(f.read(8))
f.close()
# Test alternative floating-point syntax.
print float('3.14e9'), float('-100.e-2')
# Test support for sequences of sequences/arrays.
a = [array.array('d', [-7.12, 5.23, -9.4]), array.array('d', [1

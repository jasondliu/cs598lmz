import bz2
# Test BZ2Decompressor -- this software is not hosted in the standard library
# See http://bugs.python.org/issue6050 for the gory details

import bz2

decompressor = bz2.BZ2Decompressor()

def testit():
	data = decompressor.decompress(bz2.compress(b"test"))
	assert data == b"test"
	data = decompressor.decompress(bz2.compress(b"test", 9))
	assert data == b"test"
	data = decompressor.decompress(bz2.compress(b"test", 1))
	assert data == b"test"


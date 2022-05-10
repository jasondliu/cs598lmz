from bz2 import BZ2Decompressor
BZ2Decompressor = mx.add_dict_to_class(BZ2Decompressor)

def xz_decompress(data):
	return mx.xz_decompress(data)

class GzipDecompressor(object):
	def __init__(self):
		self.closed = False
		self.decomp = zlib.decompressobj(16+zlib.MAX_WBITS)
	def decompress(self, data):
		if self.closed:
			raise ValueError( "closed decompressor" )
		if isinstance(data, bytes):
			data = bytearray(data)
		return self.decomp.decompress(data)
	def flush(self):
		if self.closed:
			raise ValueError( "closed decompressor" )
		return self.decomp.flush()
	def close(self):
		if self.closed:
			return
		self.closed = True
		self.decomp = None
	def __del__(

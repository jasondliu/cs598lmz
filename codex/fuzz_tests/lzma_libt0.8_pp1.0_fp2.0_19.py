import lzma
lzma.compress
try:
	LZMACompressor = lzma.LZMACompressor
except AttributeError:
	LZMACompressor = lzma.compress


from ._version import __version__

_no_compression = 0
_bz2_compression = 1
_lzma_compression = 2


class MyTable(Table):
	def append(self, data):
		if len(data) != self.ncols:
			raise ValueError("wrong number of columns")
		if not self.description:
			self.description = ["Column %d"%(i+1) for i in range(len(data))]
			self.formats = ["%s" for i in range(len(data))]
		self.data.append(data)
		
	def __len__(self):
		return len(self.data)
		
	def __str__(self):
		return self.pprint(max_lines=-1)
		
	def __

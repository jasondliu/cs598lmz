from lzma import LZMADecompressor
LZMADecompressor.xzmagic

import lzma
import sys

class CompressClass:
	"""This class is used to compress or decompress files or strings

	In order to compress or decompress a file or a string, use the functions
	"compressFile(), compressString(), decompressFile()" and "decompressString()".

	Example for compressing a file containing a string:

	>>> import Compress

	>>> a = Compress.compressFile("Hello\n")

	>>> a

	<lzma.LZMACompressor object at 0x7f3d770c6780>

	"""
	def __init__(self):
		self.magic = LZMADecompressor.xzmagic

	def __init__(self):
		pass

	def compressFile(self, fileName, format = "xz", filename = None):

		"""
		This function compress the file passed in the parameter named "fileName".

		The file to compress is given by the user, via the parameter named "fileName". 

		It's by default compressed by L

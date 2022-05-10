import mmap
# The size of the file that is displayed
# If this is too big, the entire contents of the file
# might not be able to be displayed.
chunkSize = 10000

class FileDisplayer(object):
	def __init__(self, filePath):
		self.filePath = filePath
		self.positionInFile = None
		self.fileHandle = None
		self.numberOfLines = None
		self.numberOfBytes = None
		self.mappingSize = None
		self.mappingOrigin = None
		self.sizeOfFile = None
		self.sizeOfFile = None
		self.sizeOfFile = None
	def __str__(self):
		return str(self.filePath)
	def __repr__(self):
		return str(self.filePath)
	def openFile(self, readOnly=False):
		"""Open the file in memory"""
		# Create the file handle
		#mode = "r" if readOnly else "r+"
		mode =

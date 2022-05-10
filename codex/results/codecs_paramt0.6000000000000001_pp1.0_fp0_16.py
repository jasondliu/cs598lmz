import codecs
codecs.register_error('strict', codecs.ignore_errors)

class TextFile:
	"""Class for reading and writing text files."""
	def __init__(self, filename, mode):
		self.filename = filename
		self.mode = mode
	
	def __enter__(self):
		self.file = codecs.open(self.filename, self.mode, encoding="utf-8")
		return self
	
	def __exit__(self, type, value, traceback):
		self.file.close()

	def read_lines(self, strip_newline=True):
		"""Reads all lines from a text file."""
		lines = []
		for line in self.file:
			if strip_newline:
				lines.append(line.strip())
			else:
				lines.append(line)
		return lines
	
	def write_lines(self, lines):
		"""Writes lines to a text file."""
		for line in lines:
			

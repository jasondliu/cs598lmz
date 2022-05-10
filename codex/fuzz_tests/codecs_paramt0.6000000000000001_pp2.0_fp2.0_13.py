import codecs
codecs.register_error('strict', codecs.ignore_errors)
codecs.register_error('replace', codecs.replace_errors)

class TextFile:
	def __init__(self, filename=None):
		self.filename = filename
		self.data = None
		if self.filename:
			self.read(filename)

	def read(self, filename):
		try:
			self.data = codecs.open(filename, "r", "utf-8").read()
		except:
			try:
				self.data = codecs.open(filename, "r", "latin1").read()
			except:
				self.data = codecs.open(filename, "r", "utf-8", 'replace').read()
			#self.data = open(filename, "r").read()
			#self.data = codecs.open(filename, "r", "utf-8", 'replace').read()

	def write(self, filename):
		codecs.

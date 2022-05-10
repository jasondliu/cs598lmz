import codecs
codecs.register_error('strict', codecs.ignore_errors)

class Source:
	def __init__(self, file_name):
		self.file_name = file_name
		self.file_desc = open(file_name, 'r')
		self.line_number = 0
		self.line = ''
		self.column_number = 0
		self.current_char = ''
		self.next_char = self.file_desc.read(1)
		self.advance()

	def advance(self):
		self.current_char = self.next_char
		self.next_char = self.file_desc.read(1)
		self.column_number += 1
		if self.current_char == '\n':
			self.line_number += 1
			self.column_number = 0
			self.line = ''

	def skip_whitespace(self):
		while self.current_char.isspace():
			self.advance()

	def read

import codecs
codecs.register_error('replace_with_space', codecs.replace_with_space)

class Utils:
	@staticmethod
	def getFileContent(path):
		with open(path, 'r', encoding = 'utf8', errors = 'replace_with_space') as f:
			return f.read()

	@staticmethod
	def getFileLines(path):
		with open(path, 'r', encoding = 'utf8', errors = 'replace_with_space') as f:
			return f.readlines()

	@staticmethod
	def writeFile(path, content):
		with open(path, 'w', encoding = 'utf8', errors = 'replace_with_space') as f:
			f.write(content)

	@staticmethod
	def writeFileLines(path, lines):
		with open(path, 'w', encoding = 'utf8', errors = 'replace_with_space') as f:
			f.writelines(lines)

	@staticmethod
	def splitFile(path, line_count):

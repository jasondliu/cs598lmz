import codecs
codecs.register_error('ignore', codecs.ignore_errors)

class Analizer():
	def __init__(self, input_file, output_file):
		self.input_file = input_file
		self.output_file = output_file
		self.analyze()

	def analyze(self):
		self.tokens = []
		self.pre_tokens = []
		self.parse_input()
		self.tokens = self.get_tokens_from_pre_tokens(self.pre_tokens)
		#print self.pre_tokens
		self.write_output()
		# for i in xrange(len(self.tokens)):
		# 	print self.tokens[i]

	def get_tokens_from_pre_tokens(self, pre_tokens):
		tokens = []
		for pre_token in pre_tokens:
			tokens.append(Token(pre_token))


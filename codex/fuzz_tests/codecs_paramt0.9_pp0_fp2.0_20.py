import codecs
codecs.register_error('surrogatepass', codecs.surrogateescape)

class stopwords:
	def __init__(self, wordlist):
		self.wordlist = wordlist

	def __getattr__(self, name):
		if name == 'wordlist':
			return self.wordlist

	def remove_stops(self, text):
		return " ".join([word for word in text.lower().split() if word not in self.wordlist])

class data_processor:
	def __init__(self, X, feature_selection = False, tfidf = False, word_tokenizer = None):
		# X should be a pandas series in the following format:
		if X.dtypes != "object":
			raise ValueError('Fields are not strings')
		self.X = X

		# Word Tokenizer
		if word_tokenizer == None:
			word_tokenizer = RegexpTokenizer(r'\w+')
		self.word_tokenizer = word_tokenizer

		#

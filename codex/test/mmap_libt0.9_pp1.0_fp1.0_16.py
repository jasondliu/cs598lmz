import mmap


class NextBinomialGenerator(object):
	"""docstring for NextBinomialGenerator"""
	def __init__(self, n = 0, p = 0.0, file_address = ""):
		self.file_to_write = open(file_address, 'wb')
		self.n = n
		self.p = p
		self.generate_all()
		self.file_to_write.close()
	def generate_all(self):
		for value in range(0, self.n + 1):
			self.file_to_write.write(pack('f', self.binomial_cdf(value)))
	def binomial_cdf(self, k):
		probability = 1
		for value in range(0, k):
			probability = probability * (1 - self.p)
		return probability

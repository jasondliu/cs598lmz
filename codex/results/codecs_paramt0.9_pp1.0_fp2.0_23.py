import codecs
codecs.register_error('replace_random', types.ReplaceRandom)

import types

class RandomByteData:
	def __init__(self):
		self.filesize = os.path.getsize('TRILOGY.dat')
		self.data_source = []
		with open('TRILOGY.dat', 'rb') as f:
			while True:
				data = f.read(1024 * 1024)
				if not data:
					break
				self.data_source.append(data)

	def read(self, size=-1):
		if self.filesize > size:
			if random.uniform(0, 1) < 0.5:
				# return random data
				return self.data_source[random.randint(0, len(self.data_source) - 1)]
			else:
				# do not return data
				return b''
		else:
			# return same data
			

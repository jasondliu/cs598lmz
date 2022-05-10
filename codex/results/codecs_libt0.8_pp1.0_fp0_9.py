import codecs
codecs.register(CustomCodec.search_function)

f = codecs.open('test.txt', 'r', encoding='custom')
print f.read()
f.close()

# 解码器,编码器,单字符解码器
class CustomIncrementalDecoder(codecs.IncrementalDecoder):
	def __init__(self):
		print 'init'
		codecs.IncrementalDecoder.__init__(self)

	def decode(self, input, final=False):
		print 'decode'
		return codecs.charmap_decode(input, self.errors, encoding_table)


def CustomIncrementalEncoder(codecs.IncrementalEncoder):
	def encode(self, input, final=False):
		print 'encode'
		return codecs.charmap_encode(input, self.errors, encoding_table)[0]


class CustomStreamWriter(codecs.StreamWriter

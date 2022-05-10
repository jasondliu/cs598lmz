import codecs
# Test codecs.register_error

def bad_encode(string):
    raise UnicodeError(string)

def bad_decode(bytes):
    raise UnicodeError(bytes)

class Codec(codecs.Codec):
    def encode(self, input, errors='strict'):
        return (bad_encode(input), len(input))

    def decode(self, input, errors='strict'):
        return (bad_decode(input), len(input))

class StreamWriter(Codec, codecs.StreamWriter):
    pass

class StreamReader(Codec, codecs.StreamReader):
    pass

def search_function(encoding):
    if encoding == 'bad':
        return codecs.CodecInfo(Codec().encode, Codec().decode,
                                StreamReader, StreamWriter)

codecs.register(search_function)

s = 'BUG'
try:
    codecs.getencoder('bad')(s)
except UnicodeError as e:
    if e.args[0] == s:
        print('Ok')
   

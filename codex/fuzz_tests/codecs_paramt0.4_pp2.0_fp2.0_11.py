import codecs
codecs.register_error('strict', codecs.ignore_errors)

# the following is borrowed from the python docs
# https://docs.python.org/2/library/codecs.html#codec-base-classes

class StreamWriter(codecs.StreamWriter):
    def __init__(self, stream, errors='strict'):
        codecs.StreamWriter.__init__(self, stream, errors)
        self.encoder = codecs.getincrementalencoder(errors)('utf-8')
        self.stream = stream

    def write(self, data):
        data, consumed = self.encoder.encode(data, self.errors)
        self.stream.write(data)
        return consumed

    def writelines(self, list):
        data = ''.join(list)
        data, consumed = self.encoder.encode(data, self.errors)
        self.stream.writelines(data)
        return consumed

    def reset(self):
        self.encoder.reset()

class StreamReader(codecs.StreamReader):
    def

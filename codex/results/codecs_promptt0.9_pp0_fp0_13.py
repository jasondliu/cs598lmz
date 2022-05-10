import codecs
# Test codecs.register_error(); Issue #1759.
class DangerousBufferedReader(codecs.BufferedReader, codecs.StreamReader):

    def __init__(self, stream, errors='strict'):
        codecs.StreamReader.__init__(self, stream, errors)
        self.stream = codecs.StreamReader.stream

    def read(self, size=-1):
        data = self.stream.read(size)
        raise RuntimeError("This should not be seen")


codecs.register_error('danger', lambda x: (x, x))
codecs.register_error('dangerous', lambda x: DangerousBufferedReader(x, 'strict'))
try:
    codecs.register_error('dangerous', lambda x: 42)
except RuntimeError as e:
    if str(e) != 'handler already registered for encoding dangerous':
        print('register_error overwrite failed:')
    else:
        raise

try:
    codecs.register_error('danger', 'danger')
except TypeError:
    pass
else:
    print('register_error failed

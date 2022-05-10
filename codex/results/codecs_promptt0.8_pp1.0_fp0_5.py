import codecs
# Test codecs.register_error for a class and a function

import codecs

class MyErrorHandler(codecs.ErrorHandler):
    def __init__(self):
        self.count = 0

    def handle_error(self, error):
        self.count += 1
        return u'A', 1

class MyError(Exception):
    pass

def my_handler(error):
    my_handler.count += 1
    return u'A', 1

my_handler.count = 0

def test(encoding, decoder_error_handler, encoding_error_handler,
         writer_error_handler):
    # Test decoder
    input = 'abc\u1234def'
    output = []
    writer = codecs.getwriter(encoding)(output.append)
    reader = codecs.getreader(encoding)(input, decoder_error_handler)
    # Read operations
    print('readline:', repr(reader.readline()))
    print('readlines:', repr(reader.readlines())[:30])
    print('read:', repr(reader.

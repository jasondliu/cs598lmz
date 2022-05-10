import codecs
# Test codecs.register_error
def bad_encode_handler(error):
    if error.object[error.start] == '\u03c0':
        return '\u03c6', error.end
    else:
        raise error

def bad_decode_handler(error):
    if error.object[error.start] == '\u03c6':
        return '\u03c0', error.end
    else:
        raise error

codecs.register_error('bad_encode', bad_encode_handler)
codecs.register_error('bad_decode', bad_decode_handler)

class CodecsRegisterErrorTest(unittest.TestCase):
    def test_register_error(self):
        self.assertEqual('abc\u03c6d', 'abc\u03c0d'.encode('ascii', 'bad_encode'))
        self.assertEqual('abc\u03c0d', b'abc\u03c6d'.decode('ascii', 'bad_decode'))

class

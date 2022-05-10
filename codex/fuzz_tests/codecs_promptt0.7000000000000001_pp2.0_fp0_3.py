import codecs
# Test codecs.register_error

def search_function(s):
    if s == 'test1':
        return codecs.lookup('iso8859-1')

codecs.register(search_function)

# This should not cause a recursion error.
'foo'.encode('test1')

# Check the registered error handler
import binascii

def hex_errorhandler(exception):
    return (u'\\x%02x' % ord(exception.object[exception.start]),
            exception.end)
codecs.register_error('test2', hex_errorhandler)

u"\x81".encode('ascii', 'test2')
# Check the registered incremental encoder

class IncrementalTestEncoder(codecs.IncrementalEncoder):
    def encode(self, input, final=False):
        return input.encode('utf-16-le')

class IncrementalTestStreamWriter(codecs.StreamWriter):
    codec = IncrementalTestEncoder

def search_function(s):
    if s == 'test3':

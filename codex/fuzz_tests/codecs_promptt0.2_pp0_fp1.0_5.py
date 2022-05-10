import codecs
# Test codecs.register_error

import codecs

def bad_decode(input, errors='strict'):
    raise UnicodeError, "bad decoding"

def bad_encode(input, errors='strict'):
    raise UnicodeError, "bad encoding"

codecs.register_error('test.bad_decode', bad_decode)
codecs.register_error('test.bad_encode', bad_encode)

# Test the error handler with a bad decoding
try:
    codecs.utf_8_decode('\xff', 'test.bad_decode')
except UnicodeError, exc:
    if str(exc) != "bad decoding":
        print "bad decoding error handler failed"

# Test the error handler with a bad encoding
try:
    codecs.utf_8_encode(u'\uffff', 'test.bad_encode')
except UnicodeError, exc:
    if str(exc) != "bad encoding":
        print "bad encoding error handler failed"

# Test the error handler with a bad decoding
try:
    codecs.utf

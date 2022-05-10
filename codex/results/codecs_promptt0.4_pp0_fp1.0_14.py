import codecs
# Test codecs.register_error

import codecs

def bad_decode(input, errors='strict'):
    raise UnicodeError

codecs.register_error('test.bad_decode', bad_decode)

assert codecs.lookup_error('test.bad_decode') is bad_decode

# Test codecs.register_error

import codecs

def bad_decode(input, errors='strict'):
    raise UnicodeError

codecs.register_error('test.bad_decode', bad_decode)

assert codecs.lookup_error('test.bad_decode') is bad_decode

# Test codecs.register_error

import codecs

def bad_decode(input, errors='strict'):
    raise UnicodeError

codecs.register_error('test.bad_decode', bad_decode)

assert codecs.lookup_error('test.bad_decode') is bad_decode

# Test codecs.register_error

import codecs

def bad_decode

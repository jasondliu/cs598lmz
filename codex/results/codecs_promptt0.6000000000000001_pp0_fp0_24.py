import codecs
# Test codecs.register_error()

# This test is intended to be run with the -v option.

import codecs
import sys

def print_error(message, filename, lineno, offset, text):
    print message
    print '    in', filename, 'line', lineno, 'offset', offset
    print '    text:'
    print text

def error_handler(message):
    print 'error_handler called with message:', message
    return (u'', 0)

def test_register():
    codecs.register_error('test.my_error_handler', error_handler)
    print 'codecs.lookup_error("test.my_error_handler"):'
    print codecs.lookup_error('test.my_error_handler')
    print 'codecs.lookup_error("test.my_error_handler")(message):'
    print codecs.lookup_error('test.my_error_handler')('message')
    print 'codecs.lookup_error("my_error_handler"):'
    print codecs.lookup

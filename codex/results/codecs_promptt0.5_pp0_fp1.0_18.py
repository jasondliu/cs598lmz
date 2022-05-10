import codecs
# Test codecs.register_error

def my_error_handler(exception):
    print "my_error_handler called"
    return (u'xyz', exception.end)

codecs.register_error('test.my_error_handler', my_error_handler)

import test.test_support

def test():
    # encoding
    for encoding, input, expected in [
        ('test.my_error_handler', 'xyz', u'xyz'),
        ('test.my_error_handler', 'x\x00yz', u'xyz'),
        ('test.my_error_handler', 'x\x00y\x00z', u'xyz'),
        ('test.my_error_handler', 'x\x00y\x00z\x00', u'xyz'),
        ('test.my_error_handler', '\x00', u'xyz'),
        ('test.my_error_handler', '', u''),
        ('test.my_error_handler', '\xff', u'xyz'),
        ('test.my_error_handler',

import codecs
# Test codecs.register_error()

import codecs

def handler(exception):
    print 'handler:', exception
    return u'\ufffd', exception.end

codecs.register_error('test.myerror', handler)

for encoding in ['ascii', 'latin-1', 'utf-8']:
    print 'Encoding:', encoding
    print repr(unicode('abc\x80def', encoding, 'test.myerror'))
    print repr(unicode('abc\x80def', encoding, 'strict'))
    print

# Encoding: ascii
# u'abc\ufffddef'
# Traceback (most recent call last):
#   File "C:\Python25\Lib\test\test_codecs.py", line 18, in <module>
#     print repr(unicode('abc\x80def', encoding, 'strict'))
# UnicodeDecodeError: 'ascii' codec can't decode byte 0x80 in position 3: ordinal not in range(128)
#
# Encoding: latin-1
#

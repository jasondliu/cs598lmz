import codecs
# Test codecs.register_error('test', lambda x: u'[warning]')
# and try to decode a string with a bad character
# in it (u'\ud800')
new_codec_error = codecs.register_error('test', lambda x: u'[warning]')
codecs.decode('test\ud800test', 'ascii', 'test')

# This is a unicode object
u'\ud800'

# This is a byte string
'\ud800'

# These are the same
u'\ud800'.encode('utf-16')
'\ud800'.decode('utf-16-be')

# This is the same as an unprintable character
# in the console
u'\ud800'.encode('utf-16-be').decode('utf-8')

# This is the same as an unprintable character
# in the console
u'\ud800'.encode('utf-8')

# Check the charset of this file
import chardet
chardet.detect(open('encoding.py', 'rb').read

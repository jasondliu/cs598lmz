import codecs
# Test codecs.register_error with the 'ignore' error handler
# Error handler is called with the following parameters:
#   exception: the exception object that was raised
#   encoding: the encoding that was being used
#   start: the start index of the unencodable bytes
#   end: the end index of the unencodable bytes
def ignore_error(exc, encoding, start, end):
    return u'', start+1
codecs.register_error('ignore', ignore_error)

s = u'abc\u20acdef'
print s.encode('utf-8', 'ignore')
print s.encode('utf-8', 'ignore')

print u"################################################################################"

import codecs
# Test codecs.register_error with the 'replace' error handler
# Error handler is called with the following parameters:
#   exception: the exception object that was raised
#   encoding: the encoding that was being used
#   start: the start index of the unencodable bytes
#   end: the end index of the unencodable bytes
def replace_error(exc, encoding, start, end

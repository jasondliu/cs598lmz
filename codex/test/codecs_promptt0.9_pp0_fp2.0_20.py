import codecs
# Test codecs.register_error('glibberish', glibberish)
# Did it work?

# The problem with the glibberish error handler is that it doesn't do
# anything useful. You should implement error handlers that translate
# the incoming bytes into a useful replacement character. Error handlers
# should take two arguments: an exception and a byte array. The exception
# is the UTF-8 decode error, and it contains information about the byte
# segment that caused the problem. The byte array is what needs to be
# translated. For example,
#
#    BadUTF8Exception(reason='bad byte', byteindex=1, start=0, end=2, object=b'\xff', encoding='utf-8')
#
# On the other hand, the byte array always starts with the first byte of
# the UTF-8 sequence that failed to decode, and includes any trailing
# bytes. Since bogus UTF-8 can have trailing bytes, our error handler
# really has to look at each byte individually. In the example above, the
# byte array is b'\xff'. The only correct thing to do with single-byte
# UTF-8 is to replace

import codecs
# Test codecs.register_error('ignore')
#
# By default, the codecs module will raise an exception when encoding or
# decoding data that cannot be converted.  With the 'ignore' error handler,
# unencodable characters are replaced by the official unicode replacement
# character, U+FFFD.
#
# The 'replace' error handler replaces unencodable characters with a question
# mark.  The 'backslashreplace' error handler inserts a backslashed escape
# sequence.  The 'xmlcharrefreplace' error handler inserts an XML character
# reference.  The 'namereplace' error handler inserts the character's name
# enclosed in angle brackets.
#
# For example, if the Unicode data '\u1234' cannot be encoded to a byte string
# in the specified encoding, the following error handlers will produce the
# following results:
#
#   ignore:       '\ufffd'
#   replace:      '?'
#   backslashreplace: '\u1234'
#   xmlcharrefreplace: '&#4660;'
#   namereplace:  '<U+1234>'
#


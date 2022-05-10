import codecs
# Test codecs.register_error('replace', '', '')
import codecs
import build

# this is the expected output for a small set of input strings for the
# 'replace','ignore','xmlcharrefreplace','backslashreplace','namereplace',
# 'surrogateescape','surrogatepass' and 'strict' error handlers.
#
# Note: the surrogateescape and surrogatepass tests are only interesting
# when running an encoding on a UCS4 build.

results = {
    # encoding, string, error handler
    ('ascii',    '\n',    'strict'): '\n',
    ('ascii',    '\x81',  'strict'): None,
    ('ascii',    '\xff',  'strict'): None,
    ('ascii',    '\x00',  'strict'): '\x00',
    ('ascii',    '\n',    'replace'): '\n',
    ('ascii',    '\x81',  'replace'): '?',
    ('ascii',    '\xff',

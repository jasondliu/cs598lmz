import codecs
# Test codecs.register_error()
encoding = 'undecodeable_encoding'

def problem_handler(exception):
    return ('undecodeable', 0), ('', exception.end)

codecs.register_error(problem_handler, 'PROBLEMM')

import encodings

encodings.search_function('undecodeable_'+encoding)

f = open(__file__, 'r')

encoding_info = encodings.getregentry(encoding)

getattr(f, encoding_info[2])(errors='PROBLEMM')

f.close()
# Test for https://bitbucket.org/pypy/pypy/issues/2479/
try:
    codecs.lookup('latin-1')
    print("lookup('latin-1') didn't fail")
except LookupError:
    pass
else:
    raise Exception("should've raised a LookupError")

try:
    codecs.lookup('123')
    print("lookup('123') didn't fail")


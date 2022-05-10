import codecs
# Test codecs.register_error

# This test should be run in an environment with the following aliases:
#
#   alias python="./python -E"
#   alias python3="./python3 -E"

from test.support import run_doctest, findfile, check_warnings
from test import support

# unicode_internal codec
def search_function(encoding):
    if encoding != 'unicode_internal':
        return None
    from test.test_support import unicode_internal_encode
    return (unicode_internal_encode, None, None)
codecs.register(search_function)

# test_search_function
def search_function(encoding):
    if encoding != 'test.test_codecs.test_search_function':
        return None
    encoder = codecs.getencoder('utf-8')
    decoder = codecs.getdecoder('utf-8')
    return (encoder, decoder, None)
codecs.register(search_function)

# test_getregentry
def search_function(enc

import codecs
# Test codecs.register_error
#
# This is a test for the register_error function, which allows custom
# error handlers to be registered.
#
# Written by Marc-Andre Lemburg (mal@lemburg.com).
#
# (c) Copyright CNRI, All Rights Reserved. NO WARRANTY.
#
# *** Check the error handler ***

def search_function(encoding):
    """ Lookup function which simulates the getregentry() API of the
        Python codec registry.
    """
    if encoding == 'test.searchfunction':
        return codecs.CodecInfo(
            name='test.searchfunction',
            encode=codecs.search_function_encode,
            decode=codecs.search_function_decode,
            incrementalencoder=codecs.search_function_incrementalencoder,
            incrementaldecoder=codecs.search_function_incrementaldecoder,
            streamwriter=codecs.search_function_streamwriter,
            streamreader=codecs.search_function_streamreader,
            )
    return None


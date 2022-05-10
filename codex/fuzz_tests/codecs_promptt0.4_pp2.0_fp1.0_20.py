import codecs
# Test codecs.register_error

# This test should be run with Python -Werror

import codecs
import encodings

# This is a test for the codecs error handling mechanism.  It
# registers a codec that raises an exception in its encode() method
# and checks that the exception is correctly propagated.

class Codec(codecs.Codec):
    def encode(self, input, errors='strict'):
        raise RuntimeError

class IncrementalEncoder(codecs.IncrementalEncoder):
    def encode(self, input, final=False):
        raise RuntimeError

class StreamWriter(Codec, codecs.StreamWriter):
    pass

class StreamReader(Codec, codecs.StreamReader):
    pass

def search_function(encoding):
    if encoding == 'test.raise':
        return codecs.CodecInfo(
            Codec().encode,
            Codec().decode,
            IncrementalEncoder,
            StreamReader,
            StreamWriter,
        )
    return None

codecs.register(search_function)

# Check that the

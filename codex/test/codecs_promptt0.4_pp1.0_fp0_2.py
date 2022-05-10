import codecs
# Test codecs.register_error

import codecs

def bad_decode(input, errors='strict'):
    raise UnicodeDecodeError("unknown", input, 0, 1, "bad")

def bad_encode(input, errors='strict'):
    raise UnicodeEncodeError("unknown", input, 0, 1, "bad")

def bad_incremental_decode(input, errors='strict'):
    raise UnicodeDecodeError("unknown", input, 0, 1, "bad")

def bad_incremental_encode(input, errors='strict'):
    raise UnicodeEncodeError("unknown", input, 0, 1, "bad")

def bad_stream_reader(stream, errors='strict'):
    raise UnicodeDecodeError("unknown", stream.read(), 0, 1, "bad")

def bad_stream_writer(stream, errors='strict'):
    raise UnicodeEncodeError("unknown", stream.read(), 0, 1, "bad")


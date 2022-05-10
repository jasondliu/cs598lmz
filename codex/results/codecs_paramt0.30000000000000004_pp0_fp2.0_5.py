import codecs
codecs.register_error('strict', codecs.ignore_errors)

def _get_encoding(stream):
    """
    Get the encoding of a stream.
    """
    if hasattr(stream, 'encoding'):
        return stream.encoding
    else:
        return 'utf-8'

def _get_encoded_stream(stream, encoding):
    """
    Get an encoded stream.
    """
    if hasattr(stream, 'encoding'):
        return stream
    else:
        return codecs.getwriter(encoding)(stream)

def _get_decoded_stream(stream, encoding):
    """
    Get a decoded stream.
    """
    if hasattr(stream, 'encoding'):
        return stream
    else:
        return codecs.getreader(encoding)(stream)

def _get_encoded_stdout(encoding):
    """
    Get an encoded stdout stream.
    """
    return _get_encoded_stream(sys.stdout, encoding)

def _get_encoded_stderr

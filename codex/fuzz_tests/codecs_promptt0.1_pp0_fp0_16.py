import codecs
# Test codecs.register_error

import codecs

def bad_decode(input, errors='strict'):
    raise UnicodeError, "bad_decode"

def bad_encode(input, errors='strict'):
    raise UnicodeError, "bad_encode"

def bad_stream_reader(stream, errors='strict'):
    raise UnicodeError, "bad_stream_reader"

def bad_stream_writer(stream, errors='strict'):
    raise UnicodeError, "bad_stream_writer"

def bad_stream_reader_buffered(stream, errors='strict'):
    raise UnicodeError, "bad_stream_reader_buffered"

def bad_stream_writer_buffered(stream, errors='strict'):
    raise UnicodeError, "bad_stream_writer_buffered"

def bad_stream_reader_buffered_line(stream, errors='strict'):
    raise UnicodeError, "bad_stream_reader_buffered_line"

def bad_stream_writer_buffered_line(stream, errors='strict'):

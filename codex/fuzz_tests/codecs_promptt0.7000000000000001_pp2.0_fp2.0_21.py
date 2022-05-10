import codecs
# Test codecs.register_error

import codecs

def bad_decode_error_handler(msg):
    print('bad_decode_error_handler:', msg)
    return ('', 0)

def bad_encode_error_handler(msg):
    print('bad_encode_error_handler:', msg)
    return ('', 0)

def bad_stream_reader(stream):
    print('bad_stream_reader:', stream)
    return codecs.StreamReader(stream)

def bad_stream_writer(stream):
    print('bad_stream_writer:', stream)
    return codecs.StreamWriter(stream)

codecs.register_error(
    'bad_decode_error_handler',
    bad_decode_error_handler
    )

codecs.register_error(
    'bad_encode_error_handler',
    bad_encode_error_handler
    )

codecs.register_error(
    'bad_stream_reader',
    bad_stream_reader
    )

codecs.register

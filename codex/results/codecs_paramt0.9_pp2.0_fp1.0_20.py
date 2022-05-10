import codecs
codecs.register_error('ColorOverflow', ColorOverflow)


class IncompleteMessage(Exception):
    pass


class Ignore(Exception):
    pass

message_ids = {}

# The only purpose of these constants, and the need to add 1, is to ensure
# backwards compatibility
INTERNAL_PROTOCOL_VERSION = 14 + 1
PROTOCOL_VERSION = 11 + 1
PROTOCOL_BUILD = 10


def decompress_data(data, compression_level=1.0):
    zlib = zlib_compressor()
    zlib.inflate(data)
    out = zlib.decompress(compression_level)
    zlib.end()
    return out.getvalue()


def compress_data(data, compression_level=1.0):
    zlib = zlib_compressor()
    zlib.compress(compression_level)
    out = zlib.flush(data)
    return out


def parse_string_msg(data):
    c = CStringIO.StringIO(data)

    len_string = c

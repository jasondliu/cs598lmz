import _struct
import zlib

comp_dict = {}

def compress(data):

    if comp_dict.get(data):
        return comp_dict.get(data)

    # 1) Get the size of the data
    # In python3 c_uint is an unsigned
    # int in C.
    data_size = _struct.pack('!I', len(data))
    compressor = zlib.compressobj()
    compressed_data = compressor.compress(data) + compressor.flush()
    compressed_size = len(compressed_data)

    # 2) Get the type of data,
    # which can only be uint16.
    data_type = _struct.pack('!H', 1)

    # 3) Compression method, which
    # can only be zlib = 1.
    compression_method = _struct.pack('!H', 1)

    # 4) Hash Identifier.
    hash_identifier = ''

    # 5) Make the compressed string.

import bz2
bz2_comp = bz2.BZ2Compressor()

def get_compressed_data(data):
    """
    Compresses the data with bz2 compression and returns the compressed data
    """
    return bz2_comp.compress(data)

def get_uncompressed_data(data):
    """
    Uncompresses the data with bz2 compression and returns the uncompressed data
    """
    return bz2.decompress(data)

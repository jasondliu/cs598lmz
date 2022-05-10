import lzma
lzma_decompress = lzma.decompress
 
def lzma_compress(data, mode=FORMAT_XZ, filter=None, check=-1, preset=None,
                  filters=None):
    """Compress data in one shot with the LZMA algorithm.

    This function is a shorthand for LZMACompressor'ing and
    'compress()'ing in one shot.

    For incremental compression, use an instance of LZMACompressor instead.

    The 'mode' parameter, if given, is the binary format of the output. This
    must be FORMAT_XZ or FORMAT_ALONE; the default is FORMAT_XZ.

    The 'filter' parameter, if given, must be a Filter instance. It is used
    to alter the compression algorithm and quite possibly reduce the
    compression ratio if you know something about the type of data you are
    compressing.

    The 'check' parameter, if given, is the integrity check to use. This
    defaults to CHECK_CRC64, which is usually a reasonable choice.

    The 'filters' parameter

import lzma
lzmaCodec = getattr(lzma, 'LZMACompressor', None)


class LZMAFilter(BaseFilter):
    """
    """

    codecs = [lzmaCodec]
    defaultCodec = lzmaCodec


class BZ2Filter(BaseFilter):
    """
    """

    codecs = [bz2.BZ2Compressor, bz2.BZ2Decompressor]
    defaultCodec = bz2.BZ2Compressor


class ZFilter(BaseFilter):
    """
    """

    codecs = [zlib.compressobj, zlib.decompressobj]
    defaultCodec = zlib.compressobj


def filterTypes():
    """
    """
    return {
        "lzma": LZMAFilter,
        "bzip2": BZ2Filter,
        "zip": ZFilter,
    }


def getFilter(filterType):
    """
    """
    filters = filterTypes()
    try:
        filter_ = filters[filterType]


import lzma
lzma_ops = {'lzma_compress':lzma.compress, 'lzma_decompress':lzma.decompress}

## Serializer-specific arguments
import lzma
lzma_ops_args = [('lzma_compress',lzma.compress,lzma.FORMAT_RAW), ('lzma_compress',lzma.compress,lzma.FORMAT_XZ), ('lzma_decompress',lzma.decompress,None)]



import zlib
zlib_ops = {'zlib_compress':functools.partial(zlib.compress, level=6), 'zlib_decompress':zlib.decompress}

## Serializer-specific arguments
import zlib
zlib_ops_args = [('zlib_compress',functools.partial(zlib.compress, level=6),9), ('zlib_compress',functools.partial(zlib.compress, level=6),1), ('zlib_comp

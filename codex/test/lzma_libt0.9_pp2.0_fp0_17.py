import lzma
lzma_ops = {'lzma_compress':lzma.compress, 'lzma_decompress':lzma.decompress}

## Serializer-specific arguments
import lzma
lzma_ops_args = [('lzma_compress',lzma.compress,lzma.FORMAT_RAW), ('lzma_compress',lzma.compress,lzma.FORMAT_XZ), ('lzma_decompress',lzma.decompress,None)]



import zlib

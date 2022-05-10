import lzma
lzma.open('test.lzma')

try:
    import bz2
    bz2.BZ2Compressor()
except ImportError:
    bz2 = None

try:
    import gzip
    import zlib
    zlib.decompressobj().flush
    gzip.GzipFile('test.gz', 'rb')
except (importError, IOError):
    gzip = None
    
#gzip.GzipFile('test.gz', 'rb')

#zlib.decompressobj().flush
#bz2.BZ2Compressor()
#lzma.open('test.lzma')

if bz2 is None or gzip is None:
    sys.exit(1)
if bz2 is None:
    sys.exit(1)
if gzip is None:
    sys.exit(1)
#if bz2 is None or gzip is None:
    #sys.exit(1)

# Error
#    if gzip is None:
#        sys.exit(1)


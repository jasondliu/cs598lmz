import lzma
lzma.decompress(open('/tmp/test.xz', 'rb').read())

# lzma.decompress(open('/tmp/test.xz', 'rb').read(), format=lzma.FORMAT_ALONE)

# lzma.decompress(open('/tmp/test.xz', 'rb').read(), format=lzma.FORMAT_XZ)

# lzma.decompress(open('/tmp/test.xz', 'rb').read(), format=lzma.FORMAT_RAW)

# lzma.decompress(open('/tmp/test.xz', 'rb').read(), format=lzma.FORMAT_AUTO)

# lzma.decompress(open('/tmp/test.xz', 'rb').read(), format=lzma.FORMAT_CHECK_UNKNOWN)

# lzma.decompress(open('/tmp/test.xz', 'rb').read(), format=lzma.FORMAT_CHECK_NONE)

#

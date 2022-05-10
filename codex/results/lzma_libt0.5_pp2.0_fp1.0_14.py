import lzma
lzma.LZMADecompressor(format=lzma.FORMAT_RAW, filters=[{'id': lzma.FILTER_ARM, 'preset': 3}]).decompress(data)
</code>


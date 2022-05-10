from lzma import LZMADecompressor
LZMADecompressor().decompress(b'...').decode('utf-8')
# 'useful information'
</code>


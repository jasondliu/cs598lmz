from lzma import LZMADecompressor
LZMADecompressor.decompress(data)

#write to file
with open('output.json', 'wb') as f:
    f.write(LZMADecompressor.decompress(data))
</code>


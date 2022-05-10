from lzma import LZMADecompressor
LZMADecompressor(format=FORMAT_AUTO, memlimit=None, check=-1)

with open(path_to_file, 'rb') as f:
    compressed_content = f.read()

decompressor = LZMADecompressor()
data = decompressor.decompress(compressed_content)
print(data)
</code>


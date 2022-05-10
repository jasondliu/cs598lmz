from lzma import LZMADecompressor
LZMADecompressorObj = LZMADecompressor()
with open('Warsztat1/wielki_lzma', 'rb') as fh:
    file_content = fh.read()
uncompressed_data = LZMADecompressorObj.decompress(file_content)
print(len(uncompressed_data))

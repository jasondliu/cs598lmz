import lzma
# Test LZMADecompressor
from lzma import LZMADecompressor

def decompress(data):
    decompress = LZMADecompressor()
    return decompress.decompress(data)

with gzip.open('/home/lucas/Documents/tweets-tweets.csv.gz', 'rb') as f:
    file_content = f.read()

uncompressed_data=decompress(file_content)

# print(uncompressed_data)
# print(len(file_content))
# print(len(uncompressed_data))

with open('/home/lucas/Documents/tweets-tweets.csv.gz.lzma', 'wb') as f:
    f.write(uncompressed_data)
</code>
Is there any other alternative to do the decompression?


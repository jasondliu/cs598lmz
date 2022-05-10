import lzma
# Test LZMADecompressor
# https://stackoverflow.com/questions/3585053/python-lzma-library-and-extracting-single-files-from-xz-files
decompressor = lzma.LZMADecompressor()
filename = 'train.csv.xz'
with open(filename, 'rb') as fh:
    file_content = fh.read()
    data = decompressor.decompress(file_content)
    print(data)

# Read LZMA file
# https://stackoverflow.com/questions/2028517/python-lzma-library-and-extracting-single-files-from-xz-files
import lzma
file_content = lzma.open('train.csv.xz', 'rt').read()
print(file_content)

# https://pypi.org/project/lz4/
# pip install lz4
import lz4
import lz4.block
# compress and decompress
compressed = lz4.block.compress(b'this

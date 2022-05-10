import bz2
# Test BZ2Decompressor
with gzip.open('/home/python/Downloads/enwiki-latest-pages-articles1.xml-p10p30302.bz2', 'rb') as f:
    file_content = f.read()
    #decompressor = bz2.BZ2Decompressor()
    #data = decompressor.decompress(file_content)

# Test LZMADecompressor
with gzip.open('/home/python/Downloads/enwiki-latest-pages-articles1.xml-p10p30302.lzma', 'rb') as f:
    file_content = f.read()
    #data = lzma.decompress(file_content)

# Test XZDecompressor
with gzip.open('/home/python/Downloads/enwiki-latest-pages-articles1.xml-p10p30302.xz', 'rb') as f:
    file_content = f.read()
    #data = lzma.decompress(file_content)
import bz2
input_file =

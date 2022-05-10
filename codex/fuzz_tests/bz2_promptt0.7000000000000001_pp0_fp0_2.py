import bz2
# Test BZ2Decompressor

bz2_decompressor = bz2.BZ2Decompressor()

bz2_decompressor.decompress(compressed_content)

# Test BZ2File

with bz2.BZ2File(bz2_file_path, 'wb') as f:
    f.write(content)
 
with bz2.BZ2File(bz2_file_path, 'rb') as f:
    decompressed_content = f.read()

 
#import gzip
# Test GzipFile

with gzip.GzipFile(gzip_file_path, 'wb') as f:
    f.write(content)

with gzip.GzipFile(gzip_file_path, 'rb') as f:
    decompressed_content = f.read()
 
#import zlib
# Test decompress

zlib.decompress(compressed_content)
 
# Test decompressobj

decompressobj = zlib.decompressobj(16 + zlib.MAX_WBIT

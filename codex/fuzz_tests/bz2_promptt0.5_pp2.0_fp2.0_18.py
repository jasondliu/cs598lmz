import bz2
# Test BZ2Decompressor

decompressor = bz2.BZ2Decompressor()

with open('data/sample_compressed_file.bz2','rb') as compressed_file:
    with open('data/sample_decompressed_file.txt','wb') as decompressed_file:
        while True:
            chunk = compressed_file.read(100)
            if not chunk:
                break
            decompressed_file.write(decompressor.decompress(chunk))
 
# Test BZ2Compressor

compressor = bz2.BZ2Compressor()

with open('data/sample_decompressed_file.txt','rb') as decompressed_file:
    with open('data/sample_compressed_file_2.bz2','wb') as compressed_file:
        while True:
            chunk = decompressed_file.read(100)
            if not chunk:
                break
            compressed_file.write(compressor.compress(chunk))
        compressed_file.write(compressor.flush())
 
# Test BZ2File

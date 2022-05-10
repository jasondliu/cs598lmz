import bz2
# Test BZ2Decompressor
import bz2

decompressor = bz2.BZ2Decompressor()

with open("files/sample.bz2", 'rb') as f:
    file_content = f.read()

uncompressed_data = decompressor.decompress(file_content)

print("File Content: ", file_content)
print("Uncompressed Data: ", uncompressed_data)

# Test BZ2Compressor

compressor = bz2.BZ2Compressor()

compressed_data = compressor.compress(b"Hello World!") + compressor.flush()

print("Compressed Data: ", compressed_data)

# bzip2 module
import bz2

# BZIP2 Compression
with bz2.BZ2File("files/sample.bz2", "w") as f:
    f.write("Hello World!")

# BZIP2 Decompression
with bz2.BZ2File("files/sample.bz2", "r") as f:
    print(f.read().dec

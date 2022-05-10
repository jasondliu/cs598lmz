import bz2
# Test BZ2Decompressor

decompressor = bz2.BZ2Decompressor()
with open("/home/david/Downloads/Toledo_Data/Toledo_Data/Toledo_Data/Toledo_Data/TOLEDO_Y2017M01D04.txt.bz2", 'rb') as f:
    compressed_data = f.read()
    decompressed_data = decompressor.decompress(compressed_data)
    print(decompressed_data)

with open("/home/david/Downloads/Toledo_Data/Toledo_Data/Toledo_Data/Toledo_Data/TOLEDO_Y2017M01D04.txt", 'wb') as f:
    f.write(decompressed_data)
    f.close()

# Test BZ2Compressor

compressor = bz2.BZ2Compressor()
with open("/home/david/Downloads/Toledo_Data/Toledo_Data/Toledo_Data/Toledo_Data/TOL

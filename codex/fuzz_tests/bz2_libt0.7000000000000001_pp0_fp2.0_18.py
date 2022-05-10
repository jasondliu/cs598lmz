import bz2
bz2.decompress(b)

#we can also use the decompress method in bz2 file object to decompress an entire file:

bz_file = bz2.BZ2File('file.bz2')
data = bz_file.read()

#The data is returned as a bytes object.
#If the compressed file is very large and we cannot fit it into memory, we can use the decompress method in a loop:

bz_file = bz2.BZ2File('file.bz2')
for data in bz_file:
    print(data)

#The decompress method can only be used once.
#we can reset the decompression by creating a new decompressor object and calling its decompress method:

bz2_decompress = bz2.BZ2Decompressor()
decompressed_data = bz2_decompress.decompress(b)
decompressed_data += bz2_decompress.decompress(b)

import bz2
# Test BZ2Decompressor
decompressor = bz2.BZ2Decompressor()
file = "NT_165182.fa.bz2"
f = bz2.BZ2File(file, 'r')
line = f.readline()
end_of_data = False
while not end_of_data:
    data = f.read(100000)
    if data == "":
        end_of_data = True
    else:
        print decompressor.decompress(data)
f.close()

# create a new decompressor
decompressor = bz2.BZ2Decompressor()

# decompress data
data = decompressor.decompress(compressed_data)

# some more decompression
data += decompressor.decompress(compressed_data2)

# finish decompression
data += decompressor.flush()

data2 = decompressor.decompress(compressed_data)
data2 == data

# bzip2 headers
file = "NT_165182.fa.bz2"
f = open(file, "rb

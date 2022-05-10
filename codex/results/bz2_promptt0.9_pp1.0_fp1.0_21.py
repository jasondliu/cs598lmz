import bz2
# Test BZ2Decompressor object
input_file_bz2 = bz2.BZ2File(input_files[0],'rb')
decompressor = bz2.BZ2Decompressor()
for i in range(10):
    nextline = input_file_bz2.readline() # read an arbitrary number of bytes
    #decompressed_data = decompressor.decompress(nextline) # 
    decompressed_data = decompressor.decompress(nextline) # 
    print(decompressed_data)
input_file_bz2.close()

# Test BZ2File object
for filename in input_files:
    with open(test_file,'rb') as f:
        decompressor = bz2.BZ2Decompressor()
        for data in iter(lambda : f.read(100 * 1024), b''): # read 100KB at a time
            decompressed_data = decompressor.decompress(data)

# Test decompress function
with open('./Combined_News_DJIA.csv','rb') as input_file:

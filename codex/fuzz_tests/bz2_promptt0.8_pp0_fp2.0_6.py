import bz2
# Test BZ2Decompressor
test = bz2.BZ2Decompressor()

# bz2.BZ2Decompressor.decompress(data)
# decompress the data, returning a bytes object containing the uncompressed data corresponding to at least data_size bytes of input. 
# If the data parameter is not provided, or None, decompresses data from the stream itself. 
# Some data may be buffered in the decompressor object.
# Changed in version 3.3: decompress() can now handle multiple concatenated compressed streams.

start = time.time()
with open(folder_path+'/train.csv.bz2', mode='rb') as file:
    file_content = file.read()
    data = test.decompress(file_content)
    data = data.decode('utf-8')
    print('Duration: {} seconds'.format(time.time() - start))
 

# let's see the results
print('\n---------- Original ----------')
print(file_content[:1000])
print('\n---------- Decompressed ----------')
print(data[:1000

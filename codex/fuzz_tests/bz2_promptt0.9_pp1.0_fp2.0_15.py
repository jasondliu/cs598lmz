import bz2
# Test BZ2Decompressor

bz2_decompressor = bz2.BZ2Decompressor()

with open('simple.html.bz2', 'rb') as input:
    filedata = input.read()
    print(filedata)
    print(type(filedata))

bz_data = bz2_decompressor.decompress(filedata)
print(bz_data)
print(type(bz_data)) 


with open('simple_decompress.html', 'w') as output:
    output.write(bz_data)

print('data written to file')

# Run from the cmd line : bzcat simple.html.bz2 | wc -c
# The output is the same as the length of the bz_data string. 

# 
# Use the following configuration:

# compresslevel = 9
# to get the smallest size. 

import bz2

encoded_data = bz2.compress(b'hello world!')
print(type(encoded_data))
print

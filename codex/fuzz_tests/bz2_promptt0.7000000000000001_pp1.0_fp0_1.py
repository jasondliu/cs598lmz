import bz2
# Test BZ2Decompressor
data = b'BZh91AY&SY.\xc8N\x18\x00\x01>_\x80\x00\x10@\x02\xff\xf0\x01\x07n\x00?\xe7\xff\xe00\x01\x99\xaa\x00\xc0\x03F\x86\x8c#&\x83F\x9a\x88PJS\x91\xf9\xf9\x89\x04\x01\x00;'

decompressor = bz2.BZ2Decompressor()

result = decompressor.decompress(data)
print(result)

# Test BZ2File
# compress
with bz2.BZ2File('lorem.bz2', 'w') as output:
    with open('lorem.txt', 'rb') as input:
        output.write(input.read())

# decompress
with bz2.BZ2File('lorem.bz2', 'rb') as input:
   

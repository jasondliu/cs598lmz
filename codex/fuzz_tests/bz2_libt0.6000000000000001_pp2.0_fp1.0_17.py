import bz2
bz2.decompress(data)

# open file for writing
f = bz2.BZ2File('sample.bz2','w')
f.write(data)
f.close()

# read from compressed file
f = bz2.BZ2File('sample.bz2')
print f.read()
f.close()

# decompress from file object
with open('sample.bz2','rb') as f:
    data = bz2.decompress(f.read())

# compress data
with open('sample.bz2','wb') as f:
    f.write(bz2.compress(data))

# compress and decompress line by line
with bz2.BZ2File('sample.bz2','r') as f:
    for line in f:
        print line

# compress and decompress data in stream
f_in = open('sample.txt','rb')
f_out = bz2.BZ2File('sample.bz2','w')
f_out.writelines(f_in

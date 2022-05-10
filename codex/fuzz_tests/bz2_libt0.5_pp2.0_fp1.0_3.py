import bz2
bz2.decompress(bz2_data)

#compress
bz2_data = bz2.compress(orig_data)
len(bz2_data)

#compress level
for i in range(1,10):
    print('{} {} bytes'.format(i,len(bz2.compress(orig_data,i))))

#decompress
bz2.decompress(bz2_data)
len(bz2.decompress(bz2_data))

#read and write
f = bz2.open('file.bz2','wt')
f.write('This is the text.')
f.close()

f = bz2.open('file.bz2','rt')
text = f.read()
text
f.close()

#compress and decompress
f = bz2.open('file.bz2','wt')
f.write('This is the text.')
f.close()

f = bz2.open('file.bz2','rt')

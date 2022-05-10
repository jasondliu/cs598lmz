import bz2
# Test BZ2Decompressor 
# Reference: http://stackoverflow.com/questions/7245012/python-decompress-and-compress-bz2-file-without-creating-a-temporary-file

# read the whole compressed file
f = bz2.BZ2File('/Users/Jian/Desktop/bz2test.bz2')
all_data = f.read()
f.close()

# decompress
dec = bz2.BZ2Decompressor()
decompressed = dec.decompress(all_data)

# check the decompressed size
print len(decompressed)

# write decompressed data to a new file
f = open('/Users/Jian/Desktop/bz2test_new.txt', 'w')
f.write(decompressed)
f.close()

# read the new file
f = open('/Users/Jian/Desktop/bz2test_new.txt', 'r')
original = f.read()
f.close()

# check the size of the new file
print len

import mmap
# Test mmap.mmap(fileno, length)
with open('test.txt', 'wb') as f:
    f.write(b'0123456789abcdef')

m = mmap.mmap(f.fileno(), 15)
m[5] = b'5'
print (m[:])
# b'01234\x356789abcdef'

m[6:] = b'6'
print (m[:])
# b'01234\x356\x36bcdef'

m.close()

# Test mmap.mmap(fileno, length, tagname)
with open('test.txt', 'wb') as f:
    f.write(b'0123456789abcdef')

m = mmap.mmap(f.fileno(), 15, tagname='ABC')
m[5] = b'5'
print (m[:])
# b'01234\x356789abcdef'

m[6:] = b'6'
print (m[:])
# b'01234\x356\x36bc

import mmap
# Test mmap.mmap over a file
# Note that to write one byte of data, you need to set a range of a page
# In other words, if you want to change byte n, you need to call mm.move(n, n, n+PAGESIZE)

f = open('test.mmap', 'w+b')
f.write(b'\0'*4096)
f.close()

f = open('test.mmap', 'r+b')
#f.write(b'\0'*4096)
mm = mmap.mmap(f.fileno(), 0)

for i in range(100):
	mm.move(i, i, i+1024)
	mm[i] = "a".encode('ascii')

print(mm[:])
mm.close()
f.close()

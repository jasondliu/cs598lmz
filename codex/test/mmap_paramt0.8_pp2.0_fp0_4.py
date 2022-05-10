import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    m[:] = bytes(2)
    # print(f.read())
	
with open('test', 'r+b') as f:
    print(f.read())

with open('test', 'rb') as f:
    m = mmap.mmap(f.fileno(), 0)
    print(m[:])

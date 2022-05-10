import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 1)
    #print(list(m))
    m.write_byte(124)
with open('test', 'rb') as f:
	print(f.read(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 1)
    print(m.length)


#print(m.find('ybob'.encode()))

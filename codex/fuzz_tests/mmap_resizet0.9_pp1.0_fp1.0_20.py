import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    print(a)
    #b = m[:]
    #print(b)
    #f.write(bytes(2))
    #c = m[:]
    #print(c)
#    m[0] = bytes(2)
#    print(m[0])
#    m.close()
#with open('test', 'r+b') as f:
#    m = mmap.mmap(f.fileno(), 0)
#    f.seek(0)
#    print(m[0])
#    m.close()

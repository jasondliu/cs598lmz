import mmap

with open('test', 'wb') as f:
    f.write(bytes(1))

with open('test', 'r+b') as f:
    m = mmap.mmap(f.fileno(), 0)
    f.truncate()
    a = m[:]
    f.truncate(4)
    b = m[:]
    # m.resize() 
    # c = m[:]
    m.close()

assert a == b
# assert a == c

print("it's ok")

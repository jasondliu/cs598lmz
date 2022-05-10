import mmap
# Test mmap.mmap object on simple-text-file.txt
f = open('simple-text-file.txt', 'r')
m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
print(m.size())
m.seek(0)  # returns 0
print(m.tell())
while True:
    line = m.readline()  # returns bytes
    if not line:
        break
    txt = line.decode()
    print(txt[:-1])
m.close()
f.close()

# test on simple-text-file
f = open('simple-text-file.txt', 'r')
m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
print(m.size())
m.seek(0)  # returns 0
while True:
    line = m.readline()  # returns bytes
    if not line:
        break
    txt = line.decode()
    print(txt[:-1])
m.close()
f.close

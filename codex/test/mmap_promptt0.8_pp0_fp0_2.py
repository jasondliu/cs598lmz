import mmap
# Test mmap.mmap object
with open("mmap.txt","r+b") as f:
    m = mmap.mmap(f.fileno(),len(f.read()))
    m[0]='a'
    s = m.readline()
    m.write("hello world\n")
    m.seek(0)
    s = m.readline()
    print(s)
    m.close()

# Another way to create mmap.mmap object
with open("mmap.txt","rb") as f:
    m = mmap.mmap(f.fileno(),len(f.read()))
    s = m.readline()
    print(s)
    m.close()

# Open a mmap.mmap object with None
m = mmap.mmap(-1,0)
m.close()

# Open a mmap.mmap object with -1
m = mmap.mmap(-1,0)
m.close()

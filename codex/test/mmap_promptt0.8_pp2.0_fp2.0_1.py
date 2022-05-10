import mmap
# Test mmap.mmap for windows
with open("somefile", "w+b") as f:
    m = mmap.mmap(f.fileno(), 0)
    m.write(b"Hello Python!\n")
    m.seek(0)
    print(m.readline())
    # b'Hello Python!\n'
    m.seek(0)
    print(m.readline())
    # b'Hello Python!\n'
    
    m.close()

# Não funciona em Windows
# print(mmap.PAGESIZE, mmap.ALLOCATIONGRANULARITY)


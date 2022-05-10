import mmap
# Test mmap.mmap.seek()
with open('mega_huge_file','r+b') as fd:
    mm = mmap.mmap(fd.fileno(), 0)
    mm.seek(mm.size() // 2)
    print(mm.tell())
 
# Test that mmap.mmap.tell() doesn't crash
with open('mega_huge_file','r+b') as fd:
    mm = mmap.mmap(fd.fileno(), 0)
    print(mm.tell())
 
# Test that mmap.mmap.read().tell() doesn't crash
with open('mega_huge_file','r+b') as fd:
    mm = mmap.mmap(fd.fileno(), 0)
    print(mm.read(mm.size() // 2).tell())
 
# Test that mmap.mmap.read().seek() doesn't crash

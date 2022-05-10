import mmap

print(mmap.PAGESIZE)
f = open('data', 'r+b')
# mm=mmap.mmap(f.fileno(), 0)
# print(mm.readline())
# mm[:4]='abcd'
# mm.flush()

s=mmap.mmap(f.fileno(),0,flags=mmap.MAP_PRIVATE,prot=mmap.PROT_READ)

print(s[:10])

s.close()
f.close()

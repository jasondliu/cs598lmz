import mmap
# Test mmap.mmap.find
nmem = mmap.mmap(0, 0)
find_list = []
find_list.append('FC  OSTEEN')
for line in nmem:
    fields = line.split()
    if fields[0] == 'FC':
        find_list.append(line[0:11])
        find_keys = ['FC', 'SR', 'JD', 'LR', 'MC', 'WR']
for thing in find_list:
    s = nmem.find(thing.encode())
    print(s)
nmem.seek(0)
print(nmem.readline())
print(nmem.tell())
nmem.seek(0, os.SEEK_END)
print(nmem.tell())
print(nmem.tell())

nmem.close()

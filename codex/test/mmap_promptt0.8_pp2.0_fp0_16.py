import mmap
# Test mmap.mmap
FILE = "/home/dell/Documents/GitHub/Python_programs/Python/mmap.txt"
#memm = mmap.mmap(f, length)
# The length has to be specified, as otherwise it uses the full length of the file
# thus file_size = len(memm)
# mmap.mmap(file.fileno(), filesize)
f = open(FILE, 'r+')
f_size = os.path.getsize(FILE)

memm = mmap.mmap(f.fileno(), f_size)
f.close()
# To close the memory map, use
# memm.close()
# The data in memory map is read as bytes, thus need to be decoded into strings
# memm.read(number_of_bytes) to read bytes, and memm.readline() to read lines

byte = memm.read(1)
print(byte)

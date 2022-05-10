import mmap
# Test mmap.mmap
# http://python3-cookbook.readthedocs.io/zh_CN/latest/c07/p17_using_memory_maps_for_sharing_memory_between_processes.html
filename = "output10"
size = os.path.getsize(filename)
f = open(filename, "rb+")
mem = mmap.mmap(f.fileno(), size)
mem[0:10]
print(mem[0:10])
mem[0:10] = b"0123456789"
print(mem[0:10])
mem[0:10] = b"0123456789"
print(mem[0:10])

# Example - Writing a Transmission Information Type
# https://stackoverflow.com/questions/12805021/python-struct-pack-how-to-write-bits
import struct

with open('output10', 'wb') as fd:
    fd.write(struct.pack('i', 0x00001f0f))


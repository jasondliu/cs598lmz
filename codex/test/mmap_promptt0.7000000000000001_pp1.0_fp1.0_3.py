import mmap
# Test mmap.mmap()

memmap_file = 'test.bin'
with open(memmap_file, 'w+b') as f:
    f.write(b'\x00' * 10)
    memmap_obj = mmap.mmap(f.fileno(), 0)

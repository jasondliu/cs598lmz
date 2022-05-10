import mmap
# Test mmap.mmap() call
with open('/usr/bin/python', 'rb', 0) as python_file:
    memory_map = mmap.mmap(
        python_file.fileno(),
        0,
        access=mmap.ACCESS_READ
    )

print(memory_map)

# Test mmap.resize() call
memory_map.resize(4096)
print(memory_map[:])

# Test mmap.read() call
memory_map.seek(0)
magic_string = memory_map.read(4)
print(repr(magic_string))

# Test mmap.close() call
memory_map.close()

import mmap
# Test mmap.mmap() issue
with open(filename, "w+") as f:
    memory_map = mmap.mmap(f.fileno(), 0)
    #print(memory_map.size())
    f.write(my_text)
    my_text_offset = 20
    print(my_text_offset)
    memory_map.seek(my_text_offset)
    print(my_text_offset)
    print(memory_map.read(16))

with open(filename, "r") as f:
    lines = f.read()
    print(lines)

# Test mmap.mmap() issue
with open(filename, "wb") as f:
    memory_map = mmap.mmap(f.fileno(), 0)
    my_text_offset = 20
    print(my_text_offset)
    memory_map.seek(my_text_offset)
    print(my_text_offset)
    memory_map.write(bytes(my_text, 'utf-8'))

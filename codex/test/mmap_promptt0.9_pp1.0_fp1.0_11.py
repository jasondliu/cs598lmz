import mmap
# Test mmap.mmap()

total = 0

def increase_region_size(size, new_size):
    global total
    data = mmap_data[:size]
    assert data == b"\0" * size
    mmap_data.resize(new_size)
    data = mmap_data[:size]
    assert data == b"\0" * size
    data = mmap_data[size:]
    assert data == b"\0" * (new_size - size)
    mmap_data.resize(size)
    total += 1

def set_value(size, index, value):
    global total
    mmap_data[index] = bytes([value])
    total += 1

size = 100
new_size = 200

with open("increase_test_file", "wb") as f:
    f.write(b"\0" * size)
    f.truncate(size)


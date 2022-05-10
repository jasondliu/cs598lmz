import mmap

if __name__ == '__main__':

    shared_memory_1 = mmap.mmap(-1, 13*1024*1024)
    #pylint: disable=no-member
    shared_memory_1.seek(0)

    offset = 1
    batch_size = 1
    workspace_name = "test"

    shared_memory_1.write(struct.pack("+B", offset))
    shared_memory_1.write(struct.pack("+B", batch_size))
    shared_memory_1.write(_str2yml(workspace_name))
    shared_memory_1.write(struct.pack("+B", offset))
    shared_memory_1.write(struct.pack("+B", batch_size))
    shared_memory_1.write(_str2yml(workspace_name))
    #pylint: enable=no-member
    shared_memory_1.seek(0)

    while True:
        offs, batch, name = _read_packed_struct(shared_memory_1)
        print(f

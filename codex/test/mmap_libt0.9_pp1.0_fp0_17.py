import mmap

if __name__ == '__main__':

    shared_memory_1 = mmap.mmap(-1, 13*1024*1024)
    #pylint: disable=no-member
    shared_memory_1.seek(0)

    offset = 1
    batch_size = 1
    workspace_name = "test"


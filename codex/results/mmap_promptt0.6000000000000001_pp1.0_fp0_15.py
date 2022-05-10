import mmap
# Test mmap.mmap vs file.read

def mmap_test():
    with open("/home/sangwook/my_dataset/big_data/big_data_tiny.txt", "r+b") as f:
        with contextlib.closing(mmap.mmap(f.fileno(), 0)) as m:
            lines = m.readlines()

    print('lines:', len(lines))
    print('lines[0]:', lines[0])

def file_test():
    with open("/home/sangwook/my_dataset/big_data/big_data_tiny.txt", "r") as f:
        lines = f.readlines()

    print('lines:', len(lines))
    print('lines[0]:', lines[0])

def performance_test():
    import time

    # MMAP
    start_time = time.time()
    mmap_test()
    elapsed_time = time.time() - start_time
    print('[MMAP] elapsed_time:', elapsed_time)

    # File


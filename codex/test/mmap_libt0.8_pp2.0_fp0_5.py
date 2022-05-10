import mmap

if __name__ == '__main__':
    print("hi")
    memory = mmap.mmap(-1, 1024, mmap.MAP_SHARED, mmap.PROT_READ | mmap.PROT_WRITE, offset=0)
    print(memory.readline())
    memory.close()

import mmap
# Test mmap.mmap.resize() method
#
# The memory mapping is created with a size of 10 bytes and then the size is
# extended to 20 bytes.

def main():
    mapping = mmap.mmap(-1, 10)
    print("mapping size: ", mapping.size())
    mapping.resize(20)
    print("mapping size: ", mapping.size())
    mapping.close()

if __name__ == "__main__":
    main()

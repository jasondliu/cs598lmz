import mmap
# Test mmap.mmap.read()

def main():
    fd = os.open("sample.bin", os.O_RDWR)
    try:
        m = mmap.mmap(fd, mmap.PAGESIZE, mmap.MAP_SHARED, mmap.PROT_WRITE)
        print "before:", `m.read(mmap.PAGESIZE)`
        m.write("x" * mmap.PAGESIZE)
        m.seek(0)
        print "after :", `m.read(mmap.PAGESIZE)`
    finally:
        os.close(fd)

if __name__ == "__main__":
    main()

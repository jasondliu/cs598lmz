import mmap
# Test mmap.mmap(fd, length=0, access=mmap.ACCESS_DEFAULT, offset=0,
#                tagname=None, flags=0, prot=mmap.PROT_WRITE)
#
# Creates a new mmap object, by default read/write.

def main():
    with open(test.support.TESTFN, "w+b") as f:
        f.write(b'x' * mmap.PAGESIZE)
        f.flush()
        fd = f.fileno()
    assert mmap.mmap(fd)


if __name__ == '__main__':
    main()

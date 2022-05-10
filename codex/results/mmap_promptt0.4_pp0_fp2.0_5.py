import mmap
# Test mmap.mmap.read()

def main():
    fd = os.open('foo.txt', os.O_RDWR | os.O_CREAT)
    os.write(fd, b'0123456789abcdef')
    os.lseek(fd, 0, 0)
    m = mmap.mmap(fd, 16, access=mmap.ACCESS_WRITE)
    print(m.read(1))
    print(m.read(5))

if __name__ == '__main__':
    main()

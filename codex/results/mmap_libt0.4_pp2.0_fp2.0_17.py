import mmap
import os

def create_mmap(filename, length):
    fd = os.open(filename, os.O_RDWR | os.O_CREAT)
    os.write(fd, bytes(length))
    os.close(fd)
    fd = os.open(filename, os.O_RDWR)
    return mmap.mmap(fd, length)

def main():
    with create_mmap("test", 1024) as mm:
        mm.write("hello")
        mm.seek(0)
        print(mm.readline())

if __name__ == "__main__":
    main()

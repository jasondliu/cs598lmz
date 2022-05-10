import mmap, os

class Mmap(object):
    def __init__(self, mode, size):
        self.mode = mode
        self.size = size

    def __enter__(self):
        fd = os.open('/dev/mem', os.O_RDWR | os.O_SYNC)
        self.m = mmap.mmap(fd, self.size, self.mode, mmap.MAP_SHARED, offset=0)
        return self.m

    def __exit__(self, type, value, traceback):
        self.m.close()

def main():
    with Mmap(mmap.ACCESS_READ, 0x1000) as m:
        print(m)

if __name__ == '__main__':
    main()

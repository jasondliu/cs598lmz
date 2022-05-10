import mmap
# Test mmap.mmap(-1, length, map_size)

def main():
    length = 8
    map_size = 4
    with mmap.mmap(-1, length) as m:
        print m.size()
        print m[:]

if __name__ == '__main__':
    main()

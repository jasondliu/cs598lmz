import mmap
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: {} <filename>".format(sys.argv[0]))
        exit(1)
    filename = sys.argv[1]

    # Open file and memory map it
    fd = os.open(filename, os.O_RDWR)
    m = mmap.mmap(fd, 0)

    # Read the file
    print("Content before mmap.move(1,0,3): {}".format(m.read(16)))

    # Move content in the memory map
    m.move(1, 0, 3)

    # Read the file again to see the modification
    print("Content after mmap.move(1,0,3): {}".format(m.read(16)))

    # Close the file and the memory map
    m.close()
    os.close(fd)

if __name__ == '__main__':
    main()

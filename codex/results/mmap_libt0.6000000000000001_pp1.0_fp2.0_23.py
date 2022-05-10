import mmap

def main():
    # Open a file
    f = open('hello.txt')

    # Create a memory-mapped file
    buf = mmap.mmap(f.fileno(), 0)

    # Close the file
    f.close()

    # Read from the memory-mapped file
    print(buf[:10])

    # Update the memory-mapped file
    buf[0:3] = b'Hey'

    # Flush changes
    buf.flush()

if __name__ == '__main__':
    main()

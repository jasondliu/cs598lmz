import mmap

def main():
    # Open a file
    fd = os.open("hello.txt", os.O_RDWR)

    # Create a memory map
    m = mmap.mmap(fd, 0, access=mmap.ACCESS_WRITE)

    # Write to the memory mapped area
    m.write("Hello Python! Love, Python.")

    # Close the open file
    os.close(fd)


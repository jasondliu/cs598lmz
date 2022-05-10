import mmap
# Test mmap.mmap() with a file name.
def main():
    fd = os.open("mapfile.txt", os.O_CREAT | os.O_RDWR)
    os.write(fd, "Hello, Python!\n")
    m = mmap.mmap(fd, 0)

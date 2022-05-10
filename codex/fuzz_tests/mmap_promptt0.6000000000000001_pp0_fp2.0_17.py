import mmap
# Test mmap.mmap()
m = mmap.mmap(-1, 13)
m.write(b"Hello, World!")
m.read(1)
m.readline()
m.seek(0)
m.read(13)
m.close()
# Test mmap.mmap() with offset
m = mmap.mmap(-1, 13, offset=42)
m.write(b"Hello, World!")
m.read(1)
m.readline()
m.seek(0)
m.read(13)
m.close()

# Test mmap.mmap() with fileno
fd = os.open("test.txt", os.O_RDWR | os.O_CREAT)
os.write(fd, b"Hello world\n")
m = mmap.mmap(fd, 13)
m.read(1)
m.readline()
m.seek(0)
m.read(13)
m.close()
os.close(fd)

# Test mmap.mmap() with fileno and offset
fd = os.open

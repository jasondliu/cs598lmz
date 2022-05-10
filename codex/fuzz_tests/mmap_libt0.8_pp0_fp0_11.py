import mmap

# Read from pipe
fd = os.open(path, os.O_RDONLY)
content = mmap.mmap(fd, 0, access=mmap.ACCESS_READ)
print content.read(1024)
content.close()
os.close(fd)

# Write to pipe
fd = os.open(path, os.O_RDWR)
content = mmap.mmap(fd, 0, access=mmap.ACCESS_WRITE)
content.write("Hello world")
content.close()
os.close(fd)

# Read from pipe
fd = os.open(path, os.O_RDONLY)
content = mmap.mmap(fd, 0, access=mmap.ACCESS_READ)
print content.read(1024)
content.close()
os.close(fd)

# Delete the pipe
os.unlink(path)
print 'deleted'
</code>
It looks as if the pipe created via the <code>os.mkfifo</code> function is not readable/writable via <code>mm

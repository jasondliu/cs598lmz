import mmap
# Test mmap.mmap(fd, length, access, offset)
shm_fd = os.shm_open(0, os.O_RDWR, 0o666)
print(shm_fd)
if shm_fd == -1:
    perror('shm_open')
    exit(-1)
shm_size = os.ftruncate(shm_fd, 1024)
if shm_size == -1:
    perror('ftruncate')
    os.close(shm_fd)
    exit(-1)
shm_ptr = mmap.mmap(shm_fd, 1024, mmap.MAP_SHARED, 0)
# Test mmap.mmap(length, flags, prot, fd, offset=0)
shm_ptr = mmap.mmap(1024, mmap.MAP_SHARED, mmap.PROT_READ | mmap.PROT_WRITE, shm_fd, 0)
# Test mmap.mmap(length, flags, prot, fd, offset=0)
shm_ptr = mmap

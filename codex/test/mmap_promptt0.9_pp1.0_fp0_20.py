import mmap
# Test mmap.mmap(-1,length) to see if it is available on the platform
try:
    mmap.mmap(-1,1).read(1)
except ValueError as e:
    if str(e) == 'cannot mmap negative file descriptor':
        raise ImportError("fcntl.ioctl() not available on this platform!")
    raise

def ioctl(arg, cmd, mutate_flag = True):
    """This use the fcntl.ioctl to perform various low level operations

    .. code ::

        import fcntl
        fcntl.ioctl(fd, cmd [,arg, mutate_flag])

    :param arg: This is the file descriptor or a buffer you read or write
    :param cmd: The special command. See <net/if.h> for more details
    :param mutate_flag: If this flag is set, the buffer is modified and returned
    """
    ret = fcntl.ioctl(arg, cmd)
    if mutate_flag:
        return arg
    return ret


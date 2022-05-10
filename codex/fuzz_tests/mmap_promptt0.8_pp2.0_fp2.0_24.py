import mmap
# Test mmap.mmap
if hasattr(mmap.mmap(0, 0), 'tell'):
    from io import DEFAULT_BUFFER_SIZE, BlockingIOError, UnsupportedOperation
    from socket import socket
    from os import SEEK_SET, SEEK_CUR, SEEK_END
    from os.path import getsize
    from io import TextIOWrapper
    from _pyio import __init__, close, flush, fileno, isatty, name,\
        mode, softspace, readable, writable, seekable
    from _pyio import __enter__, __exit__, __iter__, __next__, read, read1,\
        readinto, readinto1, readline, readlines, seek, tell, truncate,\
        write, writelines, detach
    # Test mmap.mmap
    try:
        fd = os.open(os.path.join(os.curdir, __file__), os.O_RDONLY)
    except (FileNotFoundError, PermissionError):
        pass
    else:
        fd =

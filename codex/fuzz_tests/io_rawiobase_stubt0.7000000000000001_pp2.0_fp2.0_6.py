import io
class File(io.RawIOBase): def close(self): pass
class StringIO(io.StringIO): pass

# Import constants
from io import SEEK_SET, SEEK_CUR, SEEK_END, SEEK_DATA, SEEK_HOLE, SEEK_MAX

# Import File Type
from stat import S_IFMT, S_IFREG, S_IFBLK, S_IFCHR, S_IFIFO, S_IFSOCK
from stat import S_ISREG, S_ISBLK, S_ISCHR, S_ISFIFO, S_ISSOCK

# Import flag constants for open()
from os import O_RDONLY, O_WRONLY, O_RDWR, O_EXCL, O_APPEND, O_CREAT, O_TRUNC
from os import O_DSYNC, O_RSYNC, O_SYNC, O_NONBLOCK, O_DIRECTORY, O_NOFOLLOW
from os import O_DIRECT, O_LARGEFILE, O_NOATIME, O_CLOEXEC, O_NOLINK, O_

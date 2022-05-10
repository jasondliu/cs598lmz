import _struct

from _syscall_lfs import *


##
# Constants from /usr/include/bits/stat.h.
#

S_IFMT      = 0o170000  # Bit mask for the file type bit fields.
S_IFSOCK    = 0o140000  # Socket.
S_IFLNK     = 0o120000  # Symbolic link.
S_IFREG     = 0o100000  # Regular file.
S_IFBLK     = 0o060000  # Block device.
S_IFDIR     = 0o040000  # Directory.
S_IFCHR     = 0o020000  # Character device.
S_IFIFO     = 0o010000  # FIFO.

# These don't actually exist on Linux, but are here for compatibility with
# the stat module.
S_ISUID     = 0o004000  # Set-user-ID bit.
S_ISGID     = 0o002000  # Set-group-ID bit
S_ISVTX     = 0o001000  # Sticky bit.

S

import mmap
import struct
import sys


# ============================================================================
#
# ============================================================================

def get_mem_info():
    """ Helper function to pull in meminfo.

    :returns: (bsize,total,free)
        bsize: (int) block size
        total: (int) total RAM
        free: (int) free RAM

    """
    # pull in meminfo
    with open('/proc/meminfo', 'rb') as f:
        meminfo = mmap.mmap(f.fileno(), 0, prot=mmap.PROT_READ)
    # extract block size
    bsize = int(
        meminfo[meminfo.find(b'MemTotal:') + len('MemTotal:'):].split(None, 3)[0]
    )
    # extract total and free mem
    total = int(
        meminfo[meminfo.find(b'MemTotal:') + len('MemTotal:'):].split(None, 3)[0]
    )
    free = int(
        meminfo[meminfo.find(b'MemFree:

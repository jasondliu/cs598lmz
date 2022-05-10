import _struct
from array import array
from win32api import GetFileVersionInfo, LOWORD, HIWORD

def getfsize(filename):
    """Get the size of the file at the given file system path."""
    # return the size of the file, in bytes
    return os.path.getsize(filename)

def getftime(filename):
    """Get the timestamp of the file at the given file system path."""
    # return tuple of (year, month, day, hour, minute, second)
    st = os.stat(filename)
    wt = time.gmtime(st[stat.ST_MTIME]+st[stat.ST_MTIMEZONE])
    return (wt[0], wt[1], wt[2], wt[3], wt[4], wt[5])

def getfmd5(filename):
    """Get the MD5 hash of the contents of the file at the given file
    system path."""
    # return the 32 character hex MD5 hash of the contents of the file
    m = md5.new()
    fh = file

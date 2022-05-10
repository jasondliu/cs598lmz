import mmap
import subprocess
def open_mmap(arg):
    """Opens a file with mmap on a system that supports mmap flags."""
    try:
        array_file = open(arg, "r+")
        # On Mac OSX, a file opened with mmap is writeable, but the contents
        # may not change. So, write a null character to the file to work around
        # this.
        array_file.write("\0")
        array_file.flush()
        mmap_size = os.fstat(array_file.fileno()).st_size
        mmap_file = mmap.mmap(array_file.fileno(), mmap_size, access=mmap.ACCESS_WRITE)
        return mmap_file
    except ValueError:
        return open_mmap_read(arg)

def open_mmap_read(arg):
    """Opens a file with mmap in read-only mode on a system that supports mmap flags."""
    array_file = open(arg, "r")
    mmap_size

import mmap
import os
import sys

def get_free_space_mb(folder):
    """ Return folder/drive free space (in bytes)
    """
    s = os.statvfs(folder)
    return s.f_bavail * s.f_frsize / 1048576 / 1024 # in GB

def check_consistency(path):
    print("Checking {}".format(path))
    f = open(path, "r+")
    map = mmap.mmap(f.fileno(), 0)
    if not map.read(1) == b'T':
        map.close()
        print("Inconsistent: {}".format(path))
    map.close()

def main(path):
    # list all files
    for root, dir, files in os.walk(path):
        for f in files:
            file = os.path.join(root, f)
            check_consistency(file)

    # check free space
    s = os.statvfs(path)

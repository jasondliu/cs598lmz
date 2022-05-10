import mmap
# Test mmap.mmap() can handle files larger than 2GB.
# Here, we simply try to mmap the entire file.
#
# In the shell, run
#
# python ./<scriptname> <big_2gb_file.dat>
#
# See http://bugs.python.org/issue20075

fname = sys.argv[1]

size_2gb = 2 * 1024 * 1024 * 1024

with open(fname, 'rb') as f:
    # map entire file
    m = mmap.mmap(f.fileno(), 0)


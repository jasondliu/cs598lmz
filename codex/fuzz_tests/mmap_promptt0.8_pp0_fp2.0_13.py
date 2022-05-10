import mmap
# Test mmap.mmap(fileno, length, access)
# Py_ssize_t PyString_Size(PyObject *o)
# Returns the length of the PyObject object o.
# Returns -1 on failure.
# This is equivalent to the Python expression len(o).

class Mmaper(object):
    def __init__(self, filename, access=mmap.ACCESS_WRITE):
        self.filename = filename
        self.access = access

    def __enter__(self):
        self.f = open(self.filename, "r+b")
        self.m = mmap.mmap(self.f.fileno(), 0, access=self.access)
        return self.m

    def __exit__(self, *args, **kwargs):
        self.m.close()
        self.f.close()

def run_test():
    outfile = sys.argv[1]
    with open(outfile, "wb") as f:
        f.write("\0" * 1024)
    with Mmaper(outfile) as m:
       

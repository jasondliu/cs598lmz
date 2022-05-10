import io
class File(io.RawIOBase):
    def __init__(self, fd):
        self.fd = fd
    def fileno(self):
        return self.fd

def get_file(fd):
    return File(fd)

def make_socket_socket(sock):
    return sock

# This is used in test_distutils
def get_exports_list(m):
    return m.__all__

def get_attribute(m, name):
    return getattr(m, name)

# This is used in test_distutils
def remove_dead_bytecode(dirname, verbose=0, dry_run=0):
    return

class TestCmd:
    def __init__(self):
        self.verbose = 0

def make_legacy_pyc(source):
    return source

def make_legacy_py(source):
    return source

def make_pyc(source, py_options):
    return source

def make_py(source, py_options):
    return source

def make_scripts(py_files,

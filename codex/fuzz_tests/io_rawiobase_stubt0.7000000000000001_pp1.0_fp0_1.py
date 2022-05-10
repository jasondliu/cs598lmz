import io
class File(io.RawIOBase):
    def __init__(self, name):
        self.name = name
    def read(self, size=-1):
        return open(self.name, 'rb').read()
    def readable(self):
        return True
    def writable(self):
        return False
    def seekable(self):
        return True
    def seek(self, offset, whence=io.SEEK_SET):
        return 0
    def tell(self):
        return len(self.read())
    def readline(self, size=-1):
        return self.read(size)
    def readlines(self, size=-1):
        return [self.read(size)]
    def close(self):
        pass
    def fileno(self):
        return id(self)

def generate_unknown_charmm_resname_warnings(structure, resname_mgr):
    """
    Generates warnings when a resname is not in the resname manager.
    """
    # get residues that are not in the resname manager
    # list of (chain_id,

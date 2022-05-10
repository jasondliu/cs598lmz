import io
class File(io.RawIOBase):
    def __init__(self, path, mode):
        self.f = open(path, mode)
        self.path = path
        self.mode = mode
    def close(self):
        self.f.close()
    def __getattr__(self, name):
        return getattr(self.f, name)
    def __enter__(self):
        return self
    def __exit__(self, *args):
        self.f.close()
    def __repr__(self):
        return '<File {!r} {!r}>'.format(self.path, self.mode)

import sys
if sys.version_info[0] >= 3:
    import io
    FileIO = io.FileIO
else:
    FileIO = File

def get_file_size(file_obj):
    """
    Return the size of the file object.
    """
    if hasattr(file_obj, 'size'):
        return file_obj.size
    if hasattr(file_obj, 'name'):
        try:


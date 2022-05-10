import io
class File(io.RawIOBase):
    def read(*args, **kwargs): pass
    def readinto(*args, **kwargs): pass
    def write(*args, **kwargs): pass
class SpooledTemporaryFile(*args, **kwargs):
    def __enter__(*args, **kwargs): pass
    def __exit__(*args, **kwargs): pass
    @staticmethod
    def _check(*args, **kwargs): pass
    def close(*args, **kwargs): pass
    def fileno(*args, **kwargs): pass
    def flush(*args, **kwargs): pass
    def isatty(*args, **kwargs): pass
    def read(*args, **kwargs): pass
    def readable(*args, **kwargs): pass
    def readline(*args, **kwargs): pass
    def readlines(*args, **kwargs): pass
    def seek(*args, **kwargs): pass
    def seekable(*args, **kwargs): pass
    def tell(*args, **kwargs): pass
    def truncate(*args, **kwargs): pass
    def writable(*args

import io
class File(io.RawIOBase):
    def __init__(self, *args, **kwargs):
        self.fd = io.RawIOBase.__new__(io.RawIOBase)
        self.fd.__init__(*args, **kwargs)
    def __getattr__(self, name):
        return getattr(self.fd, name)
    def __enter__(self):
        assert self.fd.fd != -1
        return self
    def __exit__(self, *args):
        self.fd.close()
        self.fd = io.RawIOBase.__new__(io.RawIOBase)
        self.fd.__init__(None)

open = File

from contextlib import contextmanager
@contextmanager
def _sigint_handler(sigint_handler, *args, **kwargs):
    import signal
    import ctypes
    old = signal.getsignal(signal.SIGINT)
    if sigint_handler:
        # Python 2 does not support keyword arguments for signal handlers.
        def handler(*args):
            return sigint_

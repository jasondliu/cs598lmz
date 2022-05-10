import io
class File(io.RawIOBase):
    
def __init__(self, name, mode='r', closefd=True,
                    opener=None):
    if mode not in ("r", "rb", "w", "wb"):
        raise ValueError()
    self.name = name
    if opener is not None:
        if not isinstance(opener, collections.Callable):
            raise TypeError
        self.opener = opener
    elif os.path.isabs(name):
        self.opener = io._LocalOpeners(1).get(os.path.isdir(name))
    else:
        self.opener = io._fdopen
    self.mode = mode
    self.closefd = closefd
    self.closed = False
    self._mode = None
    self._seekable = None
    self._tell = None
    self._last_was_write = None
```
* `self.name = name`
* `def _real_close(self, *args):
    self.closed = True
    self._do_close(self.fd)s`
* `def

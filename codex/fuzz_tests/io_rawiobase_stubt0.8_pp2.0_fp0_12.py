import io
class File(io.RawIOBase):
    def read(self, size=-1):
        return self._fd.read(size)

    def write(self, b):
        return self._fd.write(b)

    def close(self):
        ret = os.close(self._fd)
        self._fd = None
        return ret

def __init__(self, *args, **kwargs):
    self._fd = os.open(args[0], kwargs.get('mode', 'r'))
    super().__init__(self)

setattr(File, '__init__', __init__)
class BaseDir(pathlib.PurePath):
    @contextlib.contextmanager
    def _mkdir(self, mode=0o777, parents=False, exist_ok=False):
        try:
            os.mkdir(self, mode)
        except FileExistsError:
            if not exist_ok:
                raise
        except FileNotFoundError:
            if not parents:
                raise
            else:
                par = pathlib.Path(self).parent
                with par._

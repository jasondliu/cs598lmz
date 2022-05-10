import io
class File(io.RawIOBase):
    ...
    def fileno(self):
        return self._fd

    def seekable(self):
        return True

    def seek(self, offset, whence=io.SEEK_SET):
        return self._seek(offset, whence)

    def tell(self):
        return self._tell()

    def truncate(self, pos=None):
        if pos is None:
            pos = self.tell()
        try:
            return ftruncate(self, pos)
        except OSError as e:
            if e.args[0] == EINVAL:
                raise UnsupportedOperation(
                    'Files opened in append mode')
            raise


class StringIO(_TextIOBase):
    ...
    def fileno(self):
        raise OSError(errno.EBADF, 'Bad file descriptor')
    def seekable(self):
        return True

    def seek(self, pos, whence=0):
        ...

for cls in (StringIO, File):
    cls.__delete__ = _delete_method(cls.

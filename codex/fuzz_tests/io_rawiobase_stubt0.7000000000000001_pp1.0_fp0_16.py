import io
class File(io.RawIOBase):
    # ...
    ...

# python2中的写法
class File(io.RawIOBase):
    # ...
    def close(self):
        if self.closed:
            return
        # ...  # Perform any clean-up here
        # ...
        self.closed = True

# python3中的写法
class File(io.RawIOBase):
    # ...
    def close(self):
        if self._close is not None:
            self._close()
        self._close = None
        self.closed = True

# 如果你想让你的类兼容于Python2和Python3，你可以这么写
class File(io.RawIOBase):
    # ...
    def close(self):
        if self.closed:
            return
        if hasattr(self, '_close'):
            self._close()
        else:
            # Perform any clean-up here
            pass
        self.closed =

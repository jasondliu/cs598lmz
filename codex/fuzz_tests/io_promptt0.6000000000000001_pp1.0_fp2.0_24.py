import io
# Test io.RawIOBase

import _pyio as pyio

# This class is used to test RawIOBase's read() and readinto() methods
class MixinStrategy:
    def generic_read(self, n=-1):
        self.read_history.append(n)
        if n == -1:
            return b"x" * self.size
        elif n <= self.size:
            return b"x" * n
        else:
            return b"x" * self.size + b"y" * (n - self.size)

    def read(self, n=-1):
        return self.generic_read(n)

    def readinto(self, b):
        data = self.generic_read(len(b))
        n = len(data)
        try:
            b[:n] = data
        except TypeError as err:
            # If the buffer is not writeable, raise a TypeError
            if 'readonly' in str(err):
                raise TypeError("readonly buffer") from err
            else:
                # Otherwise, raise the original error


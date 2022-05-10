import io
# Test io.RawIOBase and io.BufferedIOBase by inheriting from both, and by operating
# with the base class objects.

iterable_read_methods = ['read', 'read1', 'readinto', 'readline', 'readlines']
strings_write_methods = ['write']
buffers_write_methods = ['write', 'writelines']

class MixedIO(io.RawIOBase, io.BufferedIOBase):

    def read(self, n=-1):
        return b''

    def readinto(self, b):
        return 0

    def write(self, b):
        return len(b)

    def flush(self):
        pass

class MixedIOMultiWrite(MixedIO):

    def write(self, b):
        return len(b)*2

class MixedIOMultiRead(MixedIO):

    def read(self, n=-1):
        return b'ab'

    def readinto(self, b):
        return 2


class MixedIOReader(MixedIO):

    def readable(self):
        return True

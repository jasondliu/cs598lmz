import io
class File(io.RawIOBase):
    def read(self, n=-1):
        return b"a" * n
f = File()
f.read()

f.read()

# from in_memory_test import File
# f = File()
# f.read()
# f.close()
#
#
# f.read()

# >>> import io
# >>> f = io.BytesIO(b"some initial binary data: \x00\x01")
# >>> f.read()
# b'some initial binary data: \x00\x01'
# >>> f.seek(0, 1)
# 27
# >>> f.seek(0, 2)  # seek to end of file
# 27
# >>> f.tell()
# 27
# >>> f.seek(0)
# >>> f.read()
# b'some initial binary data: \x00\x01'
# >>> f.seek(-1, 2)
# 26
# >>> f.tell()
# 26
# >>> f.read()
# b'1'
# >>> f.seek(-5, 1)
# 22

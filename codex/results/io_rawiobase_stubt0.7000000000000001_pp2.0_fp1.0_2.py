import io
class File(io.RawIOBase):
    def __init__(self, file):
        self.file = file
        self.offset = 0

    def seek(self, offset, whence=io.SEEK_SET):
        # The io module will make sure `whence` is one of the valid values.
        if whence == io.SEEK_SET:
            self.offset = offset

#     def readinto(self, b):
#         # We use `readinto` instead of `read` because the latter would
#         # require us to allocate and return a new `bytearray` object.
#         # `readinto` is a more efficient way to read the data.
#         n = self.file.readinto(b, self.offset)
#         self.offset += n
#         return n

    def readinto(self, b):
        # We use `readinto` instead of `read` because the latter would
        # require us to allocate and return a new `bytearray` object.
        # `readinto` is a more efficient way to read the data.
        try:
            n = self.

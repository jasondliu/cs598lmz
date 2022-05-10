import io
class File(io.RawIOBase):
    def readinto(self, b):
        n = len(b)
        view = memoryview(b).cast('B')
        while n > 0:
            buf = self.read(n)
            if not buf:
                break
            view[:len(buf)] = buf
            view = view[len(buf):]
            n -= len(buf)
        return len(b) - n


# class File(io.RawIOBase):
#     def readinto(self, b):
#         n = len(b)
#         view = memoryview(b).cast('B')
#         while n > 0:
#             buf = self.read(n)
#             if not buf:
#                 break
#             view[:len(buf)] = buf
#             view = view[len(buf):]
#             n -= len(buf)
#         return len(b) - n
#
#     def readall(self):
#         pass
#
#     def readable(self):
#         pass
#
#     def readinto1(self,

import io
# Test io.RawIOBase

# class RawIOBase(ABC):
#     @abstractmethod
#     def read(self, size=-1):
#         pass

#     @abstractmethod
#     def write(self, b):
#         pass

#     @abstractmethod
#     def readable(self):
#         pass

#     @abstractmethod
#     def writable(self):
#         pass

#     @abstractmethod
#     def seekable(self):
#         pass

#     def readinto(self, b):
#         data = self.read(len(b))
#         n = len(data)
#         b[:n] = data
#         return n

#     def readall(self):
#         res = bytearray()
#         while True:
#             data = self.read(DEFAULT_BUFFER_SIZE)
#             if not data:
#                 break
#             res += data
#         return res

#     def readinto1(self, b):
#         data = self.read1(len

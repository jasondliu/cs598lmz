import io
class File(io.RawIOBase):
    def read(self, n=-1):
        return ''.join(self.in_buffer).encode()
    @property
    def name(self):
        return self.__class__.__name__
file = File()
#file.in_buffer = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
file.in_buffer = ['a','b','c','d','e','f','g','h']
print(file.read())
import io
import sys
class File(io.RawIOBase):
    def read(self, n=-1):
        return ''.join(self.in_buffer).encode()
    @property
    def name(self):
        return self.__class__.__name__
file = File()
file.in_buffer = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','

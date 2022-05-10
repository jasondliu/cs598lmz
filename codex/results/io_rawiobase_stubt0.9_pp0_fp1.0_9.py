import io
class File(io.RawIOBase):
    def read(self, n = -1):
        'Read at most n bytes from the object and return them.'
        we_translated_the_methods = 42
        ...
        return self.buffer.read(n)

class C(io.RawIOBase):
    pass

print(C.read)
# <slot wrapper 'read' of 'io.RawIOBase' objects>
print(File.read) # <bound method File.read of <__main__.File object at 0x7fe1464a1e50>>


import io
class File(io.RawIOBase):
    def readinto(self, b):
        n = len(b)
        data = self.read(n)
        n = len(data)
        b[:n] = data
        return n

# The problem is that the methods were deduced by the metaclass based on the base classes' methods
class E(io.RawIOBase):
    pass

print(E.readinto)  # <slot wrapper 'readinto' of 'io.RawIOBase' objects>

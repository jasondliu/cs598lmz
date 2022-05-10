import io
class File(io.RawIOBase):
    def read(self, size=-1):
        return b"a"*size

    def readable(self):
        return True

f = File()
print(f.read(10))
print(f.read())

# In[ ]:

class File(io.RawIOBase):
    def read(self, size=-1):
        return b"a"*size

    def readable(self):
        return True

f = File()
print(f.read(10))
print(f.read())

# In[ ]:

class File(io.RawIOBase):
    def read(self, size=-1):
        return b"a"*size

    def readable(self):
        return True

f = File()
print(f.read(10))
print(f.read())

# In[ ]:

class File(io.RawIOBase):
    def read(self, size=-1):
        return b"a"*size

    def readable(self):
        return True

f = File()
print(f.read

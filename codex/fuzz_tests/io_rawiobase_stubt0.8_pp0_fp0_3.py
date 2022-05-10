import io
class File(io.RawIOBase):
    
    def __init__(self, filename):
        self.name = filename
        m = re.search(r'(?P<filename>.+)\.(?P<ext>.+)', filename)
        self.filename = m.group('filename')
        self.ext = m.group('ext')
        
    def __repr__(self):
        return 'File(name=%r, filename=%r, ext=%r)' % (self.name, self.filename, self.ext)
    
    def close(self):
        pass
    
    def readable(self):
        return True
    
    def seekable(self):
        return True
f = File('test.log')
print(f)
print(f.readable())
print(f.seekable())

print(f.name)
print(f.filename)
print(f.ext)

f.close()

# io.RawIOBase

# io.BufferedIOBase

# io.TextIOBase

# io.StringIO

# io.BytesIO



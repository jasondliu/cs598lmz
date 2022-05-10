import io
class File(io.RawIOBase):
    def __init__(self):
        self.fp = 0
    def read(self): 
        self.fp += 1
f1 = File()
f2 = File()
f1.read()
f1.read()
f1.read()
# f2.read()
f1.fp # 3
f2.fp # 1

# Use wrapper class to get clean instance
class File(io.RawIOBase):
    def __init__(self):
        self.fp = 0
    def read(self):
        self.fp += 1
        return ''
class ProxyFile(io.BufferedIOBase):
    def __init__(self):
        self.f = File()
    def read(self, *args): 
        return self.f.read(*args) 
f1 = ProxyFile()
f2 = ProxyFile()
f1.read()
f1.read()
f1.read()
f1.f.fp # 3
f2.f.fp # 0
</code>
Question:  What's the overhead of <code>File</

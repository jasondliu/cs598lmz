import io
class File(io.RawIOBase): def read(self): pass
f = File()
f.read()

class File(io.RawIOBase): def write(self, data): pass
f = File()
f.write(b'')

class File(io.RawIOBase): pass
f = File()
f.read()

class File(io.RawIOBase): pass
f = File()
f.write(b'')

class File(io.BufferedIOBase): def read(self): pass
f = File()
f.read()

class File(io.BufferedIOBase): def read(self, size): pass
f = File()
f.read()

class File(io.BufferedIOBase): def write(self, data): pass
f = File()
f.write(b'')

class File(io.BufferedIOBase): def write(self, data): pass
f = File()
f.write(b'*')

class File(io.BufferedIOBase): def seek(self, offset): pass
f = File()
f.seek(0)

class File

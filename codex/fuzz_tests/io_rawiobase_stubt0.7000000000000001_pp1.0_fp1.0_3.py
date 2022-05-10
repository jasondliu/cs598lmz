import io
class File(io.RawIOBase):
    ...
    def fileno(self):
        '''Returns underlying file descriptor if one exists.
        OSError is raised if the IO object does not use a file descriptor.
        '''
        return self._file.fileno()

# Examples of fileno
import os
os.isatty(f.fileno())
f.fileno()

# Pipe Example
import os
x, y = os.pipe()
os.write(x, b"Hello world")
os.read(y, 100)

# File descriptor example
import os
f = open("hello.txt", "w")
fd = f.fileno()
fd

# Examples of readability
import os
fd = os.open("hello.txt", os.O_RDWR | os.O_CREAT)
os.dup(fd)
os.dup2(fd, 100)
os.read(fd, 1000)

# Examples of writeability
import os
fd = os.open("hello.txt", os.O_RDWR | os.O_CREAT)
os.dup

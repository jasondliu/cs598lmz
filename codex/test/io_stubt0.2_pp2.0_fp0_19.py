import io

class File(io.RawIOBase):
    def readinto(self, buf):
        global view
        view = buf
    def readable(self):
        return True

f = io.BufferedReader(File())
f.read(1)
del f

# The buffer is still alive, and the view is still valid.
view[0] = ord('a')

# The buffer is still alive, and the view is still valid.
del view

# The buffer is still alive.
del File

# The buffer is still alive.
del io

# The buffer is still alive.
del sys

# The buffer is still alive.
del gc

# The buffer is still alive.
del __builtins__

# The buffer is still alive.
del __name__

# The buffer is still alive.
del __package__

# The buffer is still alive.
del __spec__

# The buffer is still alive.
del __loader__

# The buffer is still alive.
del __doc__

# The buffer is still alive.
del __file__

# The buffer is still alive.
del __cached__

# The buffer is still alive.
del __builtin__

# The buffer is still alive.
del __main__

# The buffer is still alive.
del __import__

# The

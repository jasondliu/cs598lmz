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

# The view should be alive
view[0] = 0

# The view should be dead
view[0] = 0

# The view should be alive
view[0] = 0

# The view should be dead
view[0] = 0

# The view should be alive
view[0] = 0

# The view should be dead
view[0] = 0

# The view should be alive
view[0] = 0

# The view should be dead
view[0] = 0

# The view should be alive
view[0] = 0

# The view should be dead
view[0] = 0

# The view should be alive
view[0] = 0

# The view should be dead
view[0] = 0

# The view should be alive
view[0] = 0

# The view should be dead
view[0] = 0

# The view should be alive
view[0] = 0

# The view should be dead
view[0] = 0

# The view should be alive
view[0] = 0

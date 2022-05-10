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

view[0] = 0

# The following line should not crash.
f.read(1)

# The following line should not crash.
f.readinto(view)

# The following line should not crash.
f.readinto(view)

# The following line should not crash.
f.readinto(view)

# The following line should not crash.
f.readinto(view)

# The following line should not crash.
f.readinto(view)

# The following line should not crash.
f.readinto(view)

# The following line should not crash.
f.readinto(view)

# The following line should not crash.
f.readinto(view)

# The following line should not crash.
f.readinto(view)

# The following line should not crash.
f.readinto(view)

# The following line should not crash.
f.readinto(view)

# The following line should not crash.
f.readinto(view)

# The following line should not crash.
f.read

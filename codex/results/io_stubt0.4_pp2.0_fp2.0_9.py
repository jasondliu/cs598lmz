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

# check that the buffer has been released
gc.collect()

# check that the buffer has been released
gc.collect()

# check that the buffer has been released
gc.collect()

# check that the buffer has been released
gc.collect()

# check that the buffer has been released
gc.collect()

# check that the buffer has been released
gc.collect()

# check that the buffer has been released
gc.collect()

# check that the buffer has been released
gc.collect()

# check that the buffer has been released
gc.collect()

# check that the buffer has been released
gc.collect()

# check that the buffer has been released
gc.collect()

# check that the buffer has been released
gc.collect()

# check that the buffer has been released
gc.collect()

# check that the buffer has been released
gc.collect()

# check that the buffer has been released
gc.collect()

# check that the buffer has been released
gc.collect()

# check that the buffer has been released
gc.collect()

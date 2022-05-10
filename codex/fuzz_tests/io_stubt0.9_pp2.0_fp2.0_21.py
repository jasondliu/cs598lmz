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

# PROBY DELETE
view = None
# PROBY CLEANUP
del view

# You might expect (file instance) to be garbage collected here.
# However, the PEP3121 file wrapper object holds a reference to view and thus is not
# collected.

# PROBY DELAY

for i in range(3):
    f = io.BufferedReader(File())
    f.read(1)
    del f

view = None

# Now the wrapper is reachable from the type. You would expect that free it up and allow
# collection of the wrapper. However, a different path is followed.
# File.closed becomes a spesh guard here, but that requires access to co_code, which is a
# python level attribute on code objects. Thus, the wrapper is kept alive to be kept as the
# caching for accessing co_code but then that is never used because the function does not
# return again.

# PROBY DELAY

class File(io.RawIOBase):
    def readinto(self, buf):
        global view
        view = buf

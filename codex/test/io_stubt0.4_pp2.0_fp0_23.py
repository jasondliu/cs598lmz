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

print(view)

# io.BufferedReader.readinto() calls io.BufferedReader.readinto1() which calls io.BufferedReader.read1()
# which calls io.BufferedReader.raw.readinto() which calls File.readinto() which sets view.
# view is then deleted in the del f line.
# The reference to view is then used in the print(view) line.

# This is a use-after-free bug.

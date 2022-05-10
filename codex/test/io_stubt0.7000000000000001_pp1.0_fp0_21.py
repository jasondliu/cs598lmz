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

###############################################################################
# io.RawIOBase.readline
###############################################################################

class File(io.RawIOBase):
    def readline(self, limit=-1):
        global view
        if limit == -1:
            return view
        else:
            return view[:limit]
    def readlines(self, hint=-1):
        return [view]
    def readable(self):
        return True

f = io.BufferedReader(File())
del f

###############################################################################
# io.BufferedReader.readline
###############################################################################

class File(io.RawIOBase):
    def readinto(self, buf):
        global view
        view = buf
    def readline(self, limit=-1):
        global view
        if limit == -1:
            return view
        else:
            return view[:limit]
    def readable(self):
        return True

f = io.BufferedReader(File())
f.read(1)
del f
print(view)


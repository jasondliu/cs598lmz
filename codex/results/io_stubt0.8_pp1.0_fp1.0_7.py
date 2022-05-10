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

gc.collect()

print(gc.get_referrers(buf))

# get_referents because this will work only after at least one collection
# gc.get_referrers(buf) == [view]

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

#__main__.File() is not in reference cycle anymore
gc.collect()

print("All objects are collected")
# SomeFile object is not included in current collected objects
print(gc.collect())
print(gc.get_objects())

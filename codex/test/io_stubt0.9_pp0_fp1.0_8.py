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
del File

def run():
    for count in range(1000):
        for i in view:
            pass

run()
run()
run()

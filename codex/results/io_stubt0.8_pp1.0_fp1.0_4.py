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
import os

os.spawnvp(os.P_NOWAIT, "ls", ["ls"])

os.spawnlp(os.P_NOWAIT, "ls", "ls", "-l")

os.spawnl(os.P_NOWAIT, "ls", "ls", "-l", "/etc/hosts")

os.spawnle(os.P_NOWAIT, "ls", "ls", "-l", "/etc/hosts", {"HOME": "/etc"})
import tempfile

fd, name = tempfile.mkstemp()

tmpf = os.fdopen(fd, "w+b")
tmpf.write(b"one\n")
tmpf.write(b"two\n")
tmpf.write(b"three\n")
tmpf.flush()
import os

os.fsync(fd)
size = os.fstat(fd).st_size

tmpf.seek(0)

assert tmpf.read() == b"one\ntwo\nthree\n"



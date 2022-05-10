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
sys.stdout.buffer.write(view)
""")
        self.check_python("""
import sys

view = None

class File:
    def readinto(self, buf):
        global view
        view = buf
    def readable(self):
        return True

f = sys.stdin.buffer
f.RawIOBase.readinto = File().readinto
del f
sys.stdout.buffer.write(view)
""", """
import sys

view = None

class File:
    def readinto(self, view):
        self.view = view
    def readable(self):
        return True

f = sys.stdin.buffer
f.RawIOBase.readinto = File().readinto
f.read(1)
del f
sys.stdout.buffer.write(f.RawIOBase.view)
""")

    def test_sys_stdin_readinto(self):
        self.check_python("""
import sys
buf = bytearray(10)
sys.stdin.buffer.readinto(buf

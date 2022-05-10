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

# issue #10
import os
os.set_blocking(0, True)
os.set_blocking(0, False)

# issue #12
import sys
sys.stdout.write('a\n')

# issue #13
import time
time.sleep(1)

# issue #15
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 80))
s.send('GET / HTTP/1.0\r\n\r\n')
print s.recv(1000)
s.close()

# issue #16
import os
os.urandom(4)

# issue #19
class C(object):
    def __repr__(self):
        return 'C()'

print C()

# issue #22
import os
os.environ['a'] = 'b'

# issue #26
import sys
print sys.version_info

# issue #27
import os
os.exit(0)


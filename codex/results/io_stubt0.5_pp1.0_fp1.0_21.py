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

# Test for issue #4202

# Try to crash the interpreter
import sys
sys.stdout = sys.stdin = sys.stderr = open(__file__, 'rb')

# Test for issue #4203

# Try to crash the interpreter
import sys
sys.stdout = sys.stdin = sys.stderr = open(__file__, 'wb')

# Test for issue #4204

import sys
sys.stdout = sys.stdin = sys.stderr = open(__file__, 'w')

# Test for issue #4205

# Try to crash the interpreter
import sys
sys.stdout = sys.stdin = sys.stderr = open(__file__, 'r')

# Test for issue #4206

# Try to crash the interpreter
import sys
sys.stdout = sys.stdin = sys.stderr = open(__file__, 'a')

# Test for issue #4207

# Try to crash the interpreter
import sys
sys.stdout = sys.stdin = sys

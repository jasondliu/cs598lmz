import io
class File(io.RawIOBase):
    def __init__(self, f):
        self.f = f
    def read(self, n=-1):
        return self.f.read(n).encode()
    def write(self, b):
        return self.f.write(b.decode())

with open('test_file', 'w') as f:
    print(f.write('hello'))

with File(open('test_file', 'r')) as f:
    print(f.read())

# ######################################################################################################################

# io.StringIO
# io.BytesIO
# io.StringIO()
# io.BytesIO()

# ######################################################################################################################

# io.BufferedIOBase
# io.BufferedReader
# io.BufferedWriter
# io.BufferedRWPair
# io.BufferedRandom

# ######################################################################################################################

# io.TextIOBase
# io.TextIOWrapper
# io.StringIO()
# io.BytesIO()

# ######################################################################################################################


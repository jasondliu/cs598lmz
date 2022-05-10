import io
class File(io.RawIOBase):
    def __init__(self, file):
        self.file = file
    def read(self, n=-1):
        return self.file.read(n).encode('latin-1')
    def write(self, b):
        return self.file.write(b.decode('latin-1'))
    def close(self):
        return self.file.close()
    def flush(self):
        return self.file.flush()

import sys
if sys.version_info[0] < 3:
    sys.stdin = File(sys.stdin)
    sys.stdout = File(sys.stdout)
    sys.stderr = File(sys.stderr)

import os
import sys

#sys.path.append(os.path.dirname(__file__))
#sys.path.append('/Users/carlos/Documents/GitHub/Algoritmos3/TP3/src/')

cont=0

class Vertice:
	def __init__(self, nombre):
	

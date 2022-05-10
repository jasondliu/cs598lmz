import mmap
# Test mmap.mmap and mmap.mmap.write

f = open('joke.txt')
m = mmap.mmap(f.fileno(), 0)
(m.find(b'how'), m[:5], m[5:10], m[-5:])

m[5:10] = b'hahaha'
m.seek(0)
m.readline()

m.close()
f.close()
class f(object):
   def __init__(self):
      self.fd = sys.stdin.fileno()
   def fileno(self):
      return self.fd

m = mmap.mmap(f().fileno(), 0)
m.write_byte(b'E')
f = open('joke.txt')
m = mmap.mmap(f.fileno(), 0)
(m.find(b'how'), m[:5], m[5:10], m[-5:])
m.seek(0)
m.find(b'how')
m = mmap.mmap(f.fileno(),

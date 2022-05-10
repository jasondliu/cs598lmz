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
del view
gc.collect()

if sys.version_info >= (3,):
    sys.stdout.buffer.write(b'x')
else:
    sys.stdout.write('x')
    sys.stdout.flush()

def getsize(ob):
    return os.path.getsize(ob.__dict__['name'])
def getlen(ob):
    return len(ob._reader.raw)

l = []
for i in range(200):
    l.append(io.BufferedRandom(io.BytesIO()))
if sys.version_info >= (3,):
    size1 = sum(getsize(ob) for ob in l)
else:
    size1 = sum(getlen(ob) for ob in l)
del l
gc.collect()

l = []
for i in range(200):
    l.append(io.BytesIO())
size2 = sum(getsize(ob) for ob in l)

#io.DEFAULT_BUFFER_SIZE is defined in
#Modules/io/buff

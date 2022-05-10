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
print(view)
</code>
I know there's an obvious way of doing this, but I'm not able to squeeze it out.


A:

Answering my own question... I couldn't figure out how to "tell" <code>bdb</code> to call the <code>readinto</code> method. But <code>Pdb</code> can do just that. It has a <code>display</code> command that will call the method on the object.
<code>import bdb
import io

class File(io.RawIOBase):
    def readinto(self, buf):
        global view
        view = buf
    def readable(self):
        return True
    def read(self, size):
        return self._file.read(size)

f = io.BufferedReader(File())

pdb = bdb.Pdb(stdin=None, stdout=None)
pdb.run('f.read(1)')
pdb.run('display')
</code>


import mmap
import shutil
import tempfile

class MyTempFile(tempfile.NamedTemporaryFile):
    _marked = False
    def mark(self):
        self._marked = True

    def close(self):
        if not self._marked:
            super(MyTempFile, self).close()

fout = MyTempFile(delete=False)
try:
    fout.write("xxx")
    fout.flush()
    with open(fout.name, "r+b") as fin:
        mm = mmap.mmap(fin.fileno(), 0, mmap.ACCESS_WRITE)
        mm.resize(mm.size() * 2)
    fout.mark()
finally:
    fout.close()
</code>
You have now doubled the size of your file and you have access to the file data in your <code>mm</code> object. 


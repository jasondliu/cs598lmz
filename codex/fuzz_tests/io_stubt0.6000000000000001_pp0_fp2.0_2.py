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
</code>
This script is crashing with <code>Segmentation fault</code> on 3.2.3 and 3.3.0rc2.
As a workaround I can use <code>io.BytesIO</code> instead of <code>File</code>, but the question is why this crash happens and what is the correct way to write a replacement for <code>file</code> object?


A:

The issue is that <code>BufferedReader.read</code> calls <code>self.raw.readinto</code>, not <code>self.raw.read</code>.  So, your <code>File.read</code> method is never called.  You might be able to use <code>io.BufferedRWPair</code> instead, which calls <code>self.reader.read</code>.


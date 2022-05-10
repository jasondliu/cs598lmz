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
print(view) # memoryview(bytearray(b'*'))
del view
</code>
And it doesn't work: just before <code>readinto()</code> is called, <code>view = buf</code> isn't a reference anymore.
Actually, if we look at the CPython source for buffered.c, we can see that the code indeed does exactly this type of assignment:
<code>buf = self._get_read_buffer()
nbytes = self._read_buf(buf, memory)
</code>
If we look at ceval.c, <code>TARGET(LOAD_GLOBAL)</code> is essentially <code>POP()</code>, so <code>self._read_buf(buf, memory)</code> causes the value <code>buf</code> to get overwritten with the return value of that function call, causing a new reference to the temporary buffer to get destroyed even before <code>self.readinto(self._read_buf(buf))</code> happens, which then sets <code>view</code> to something else which may eventually get garbage collected.
This

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
gc.collect()
</code>
I get this output:
<code>$ python3.2 gc.py
gc: collecting generation 0...
gc: collecting generation 1...
gc: collecting generation 2...
gc: collecting generation 0...
gc: collecting generation 1...
gc: collecting generation 2...
</code>
The bug appears to be in the <code>threading</code> module, which uses <code>PyBuffer_FromReadWriteMemory()</code> to create a <code>Py_buffer</code> instance from a memory block. The <code>PyBuffer_FromReadWriteMemory()</code> function does not call <code>PyObject_GC_UnTrack()</code>. Unless I am mistaken, this means that the <code>Py_buffer</code> object is not added to the garbage collector's list of objects.
Either the <code>PyBuffer_FromReadWriteMemory()</code> function should be modified to call <code>PyObject_GC_UnTrack()</code> when a new Python object is created, or the <code>PyBuffer_Release()</code> function needs to call <code>

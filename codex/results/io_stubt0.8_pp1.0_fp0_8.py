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
view
</code>
The data in <code>buf</code> passed to <code>readinto</code> is garbage(<code>\xbe</code> in my case), but in CPython on macOS 10.11.6 it is <code>\x00</code>. I think it is because that in CPython on macOS, the <code>PyObject_Malloc</code> returns the memory allocated by <code>mmap</code> with <code>PROT_WRITE</code> and <code>PROT_EXEC</code> when the size is one page or more (in bytes), but in MicroPython on macOS, it never returns the memory with <code>PROT_EXEC</code>, so the memory of <code>buf</code> is neither <code>PROT_WRITE</code> nor <code>PROT_EXEC</code>.


A:

The behaviour is different because you're using different compilers.
Most likely your default Python 3 is compiled with Apple's clang compiler and your MicroPython is compiled with gcc.
The reason that the value of buf is different is because of different implementations

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
print(view.__array_interface__)
print(view.__array_interface__['data'])
</code>
It works fine on CPython, but on PyPy, it gives:
<code>&lt;memory at 0x7f93ea8d8d08&gt;
{'data': (18446744073709551615, False), 'typestr': '|u1', 'descr': [('', '|u1')], 'shape': (1,), 'strides': None, 'version': 3}
(18446744073709551615, False)
</code>
As you can see, PyPy gives me a garbage value for the pointer. I could just cast the pointer to <code>void*</code> and then to <code>uintptr_t</code> but I don't even know if this would work.
So, is there a way to get the pointer to a Python buffer from PyPy?


A:

You can access the memory location of the buffer using the <code>__buffer__</code> attribute.
<

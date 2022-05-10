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
del File
view
</code>
The code above shows that the Python object created by the <code>File.__new__</code> method is actually freed, while the Python object returned by <code>io.BufferedReader.__new__</code> is not freed.
The way I see this happening is that <code>PyType_GenericNew</code> is calling <code>is_instance(tp, &amp;PyType_Type)</code> when the <code>tp</code> argument is a <code>PyTypeObject</code>, which is the case for <code>File</code>. The result of this test is <code>0</code>, so the <code>Peer</code> constructor is not called and the <code>RawIOBase</code> object, which has no Python object associated with it (<code>_base.__dict__ is None</code>), is freed, which is normal since it is a Python object created by a <code>__new__</code> method.
Does anyone know the reason why <code>PyType_GenericNew</code> is not calling <code>Peer.__new__

import io
class File(io.RawIOBase):
    def __init__(self, fobj):
        self._fobj = fobj
</code>
So that <code>file</code> is a <code>RawIOBase</code> object.
Why doesn't python just do <code>self = fobj</code>?
I think this requires more knowledge about how python's object model works. 


A:

<code>io.RawIOBase</code> is an abstract base class. It defines the interface that all classes that inherit it must implement. That is, a class can only inherit <code>io.RawIOBase</code> if it implements all the methods defined in its interface.
The <code>File</code> class defined in the standard library does not inherit from <code>io.RawIOBase</code>, but rather from <code>_io.FileIO</code>. The <code>_io</code> module is a C extension module, so we can't directly see its source code, but we can find out more about it by inspecting its type:
<code>&gt;&gt;&gt; import _io
&gt;&gt;&gt

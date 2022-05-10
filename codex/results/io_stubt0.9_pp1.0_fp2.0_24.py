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
view  # [Name] is still alive, or it can be collected before the next del...
del view
</code>
You could also check if <code>[Name]</code> is a nested <code>capsule</code> object (it's a C extension), using code like the following:
<code>import types

if type(view) is types.CapsuleType and view.__name__ == 'numpy.core._internal._NDArray_fields'):
    # It's a numpy array, requiring numpy to be installed.
    import numpy
    typed_view = numpy.get_view_as_type(view, numpy.uint8)
    # Delete the capsule object before converting it to bytes object.
    del view
    byte_view = bytes(typed_view)
    del typed_view
    byte_view
else:
    byte_view = bytes(view)
    del view
    byte_view
</code>


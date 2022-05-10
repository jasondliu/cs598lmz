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
To do an effective test, your use case somehow has to make sure the <code>io.BytesIO</code> object is still around until the GC cycle that collects the <code>200 million</code> objects that you're stuffing into <code>buf</code>.  If you have that much data in a single <code>buf</code>, you're likely to have quite a few other global references to various objects in that data as well.  You don't go into any detail about how you're using this, so I'm not going to second guess your design -- and it really seems like you need to not implement your custom ReadableFile using <code>RawIOBase</code> anyway since it is "intended to be used for direct access to low-level device," and you're implementing a virtual data storage module, aren't you?  I can't speak to all of the repercussions of such a subclassing, but it seems like your use case is exactly what <code>BytesIO</code> is for (to create a view into an array), even if it is not exactly what you'd use in a production module.


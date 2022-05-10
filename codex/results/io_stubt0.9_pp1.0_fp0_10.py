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
view[0]
</code>
As a side note: <code>gobject.idle_add(method)</code> is correct, <code>gobject.idle_add(method())</code> is incorrect, it would only invoke <code>method</code> exactly once (when you call <code>idle_add</code>) and pass its return value to <code>idle_add</code>.
If you want to make a buffer object without copying the memory, consider using <code>ctypes</code>:
<code>from ctypes import *

# access mpv's internal libmpv api
libmpv = CDLL("libmpv.so.1")

# the libmpv API uses void* for byte data
void_ptr = POINTER(c_char)

# this will be the destination for mpv's "video-out-params" event, which
# contains information about the video frame that was just received
class VideoOutParams(Structure):
    _fields_ = [
        # video frame properties
        ("w", c_int), ("h

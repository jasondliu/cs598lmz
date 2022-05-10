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

print(view[:1])

def get_buffer(obj, obj_id):
    import gc
    for referrer in gc.get_referrers(obj):
        if id(referrer) == obj_id:
            return referrer

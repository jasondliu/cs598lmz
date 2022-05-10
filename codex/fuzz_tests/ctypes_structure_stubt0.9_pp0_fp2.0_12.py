import ctypes

class S(ctypes.Structure):
    x = ctypes.c_int
    _fields_ = ("x", ctypes.c_int), ("fp", ctypes.c_void_p),

class E:
    def __init__(self, fp):
        self.x = "test"
        self.fp = fp

    def __del__(self):
        print("del", self.x)
        self.fp()

for i in range(2):
    fd = os.open("e", os.O_CREAT | os.O_TRUNC | os.O_WRONLY, 0644)
    os.write(fd, b"\x01" * 0x400)
    os.close(fd)
    fd = os.open("e", os.O_RDWR)
    e = E(lambda: os.close(fd))
    mmap.mmap(fd, 0x400, 0, mmap.MAP_SHARED).write(p8(-1))

os.unlink("e")

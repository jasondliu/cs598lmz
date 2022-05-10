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

# CHECK: view =
# CHECK-NEXT: 0x{{.+}}
# CHECK-NEXT: 0x{{.+}}
# CHECK-NEXT: 0x{{.+}}
# CHECK-NEXT: 0x{{.+}}
# CHECK-NEXT: 0x{{.+}}
# CHECK-NEXT: 0x{{.+}}
# CHECK-NEXT: 0x{{.+}}
# CHECK-NEXT: 0x{{.+}}
# CHECK-NEXT: 0x{{.+}}
# CHECK-NEXT: 0x{{.+}}
# CHECK-NEXT: 0x{{.+}}
# CHECK-NEXT: 0x{{.+}}
# CHECK-NEXT: 0x{{.+}}
# CHECK-NEXT: 0x{{.+}}
# CHECK-NEXT: 0x{{.+}}
# CHECK-NEXT: 0x{{.+}}
# CHECK-NEXT: 0x{{.+}}
# CHECK-NEXT: 0

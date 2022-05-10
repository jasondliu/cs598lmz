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

b = bytearray()
len(b)
b += view
len(b)

compile(b, "<input>", "exec")

""")

def load_opcode(opnum):
    bc = bytearray()
    bc += b"\0\0\0\0\0" * 4 * 256
    bc[0] = opnum
    bc += b"\0" * 5
    compile(bc, "<opcode>", "exec")

load_opcode(opcode.opmap["LOAD_FAST"])
load_opcode(opcode.opmap["LOAD_GLOBAL"])
load_opcode(opcode.opmap["LOAD_NAME"])
load_opcode(opcode.opmap["LOAD_CONST"])
load_opcode(opcode.opmap["STORE_FAST"])
load_opcode(opcode.opmap["STORE_GLOBAL"])
load_opcode(opcode.opmap["STORE_NAME"])

def load_bad_opcode

import ctypes
# Test ctypes.CFUNCTYPE()
print type(cfptr_int(1))

f = cfptr_int(1)
print f()
print cfptr_int(None)(1)

print int(1 + 32)
print int("1") == 1
print int("011")
print int("011", 8) # in python 3, int("011", 8) gives "syntax error"
print int("1010", 2) # binary
print int("A", 16)
int("0xff", 16)
print int("0xFF", 16)
print int("0xcafe", 16)

def cstr_in(cstr):
    print "Buffered String:\n -> %d %d %d %d %d %d %d %d %d %d %d %d " % (
        cstr[0], cstr[1], cstr[2], cstr[3], cstr[4], cstr[5], cstr[6],
        cstr[7], cstr[8], cstr[9], cstr[10], cstr[11])
    print " -> %d %d %

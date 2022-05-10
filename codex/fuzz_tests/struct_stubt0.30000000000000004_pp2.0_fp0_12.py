from _struct import Struct
s = Struct.__new__(Struct)
s.format = '>I'
s.size = 4
s.pack(0x41414141)

# 0x08048d0d : pop ebp ; ret
# 0x08049a21 : pop ebx ; pop esi ; pop edi ; pop ebp ; ret
# 0x08048d0e : xchg eax, ebp ; ret
# 0x08049a22 : xchg eax, ebx ; ret
# 0x08049a23 : xchg eax, ecx ; ret
# 0x08049a24 : xchg eax, edx ; ret
# 0x08049a25 : xchg eax, esi ; ret
# 0x08049a26 : xchg eax, edi ; ret
# 0x08048d0f : mov eax, dword ptr [eax] ; ret
# 0x08048d10 : mov eax, dword ptr [ebx] ; ret
# 0x08048d11 : mov eax, dword ptr [ecx] ; ret
# 0x080

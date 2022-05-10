from _struct import Struct
s = Struct.__new__(Struct)
s.__init__('i')

def unpack(data):
    return s.unpack_from(data)

# https://github.com/mist64/x86_64asm.py/blob/master/x86_64asm.py
def pack(data):
    return s.pack(data)

# https://github.com/trezor/trezor-mcu/blob/master/firmware/bootloader/bootloader_utils.c
def reverse_crc32(word):
    crc = 0xFFFFFFFF
    for i in range(32):
        cur_bit = 1 if (word & 0x80000000) else 0
        cur_bit ^= crc & 0x01
        crc = (crc >> 1) & 0x7FFFFFFF
        if cur_bit:
            crc ^= 0xEDB88320
        word = (word << 1) & 0xFFFFFFFF
    return crc


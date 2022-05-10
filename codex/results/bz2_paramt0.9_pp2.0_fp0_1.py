from bz2 import BZ2Decompressor
BZ2Decompressor(max_length=131072).decompress((b'x\x9c+\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                                              b'\x00\x00\x04$\x00\x03\x00\x03\x00\x04\x00\x05\x00'
                                              b'\x04\x00\x04\x00\x00\x00\x00\x01'))
#=> b'0123456789abcdef'
BZ2Decompressor(max_length=131072).decompress((b'x\x9c+\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
                                              b'\x00\x00\x04$\x00\x03\x00\x03\x00\x04\x00\x05\x00'
                                              b'\x04\x00

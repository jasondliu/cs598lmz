from _struct import Struct
s = Struct.__new__(Struct)
s.load(io.BytesIO(b'\x01\x02\x03\x04'))
print(s.format)
print(s.size)
print(s.unpack('!H', b'\x02\x01'))

# 祵報録報逑話汽衸報肥逑排報。
# >>> from _compression import compress, decompress
# >>> compress(b'witch which has which witches wrist watch')
# b'\x78\x9c\xcbH\xcd\xc9\xc9W(\xcf/\xcaI\x01\x00<H2\x04\x00'
# >>> decompress(compress(b'witch which has which witches wrist watch'))
# b'witch which has which witches wrist watch'

# 祵報録報逑綬話汽衸報肥逑排報。
# >>>

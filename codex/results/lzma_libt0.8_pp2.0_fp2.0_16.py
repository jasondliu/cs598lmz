import lzma
lzma.init()
print(lzma.is_check_supported(lzma.CHECK_CRC64))

data = b"1234567890" * 1000
comp = lzma.compress(data, presets=lzma.PRESET_EXTREME)

# Here's the issue. comp is a string.

ret = lzma.decompress(comp, format=lzma.FORMAT_RAW)
print(ret)
print(ret == data)
ret = lzma.decompress(comp, format=lzma.FORMAT_XZ)
print(ret)
print(ret == data)
ret = lzma.decompress(comp)
print(ret)
print(ret == data)
</code>
This code outputs:
<code>True
b'1234567890'
False
b'\xfd7zXZ\x00\x00\x04\xe6\xd6\xb4F\x02\x00!\x01\x16\x00\x00\x00t/\

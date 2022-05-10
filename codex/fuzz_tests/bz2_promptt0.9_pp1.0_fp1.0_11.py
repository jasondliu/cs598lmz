import bz2
# Test BZ2Decompressor.eof
b = bz2.BZ2Decompressor()
print(b.eof)			# 1
print(b.decompress(b"xxx"))			# 3
print(b.eof)			# 0
print(b.decompress(b"yyy\x00"))	# 4
print(b.eof)			# 1

with bz2.open("test.bz2") as f:
    with open("test.out", "wb") as outf:
        while 1:
            data = f.read(100)
            if not data:
                break
            outf.write(data)

import bz2
# Test BZ2Decompressor

def dstream(decompressor):
    data = b"",
    while True:
        data = data + decompressor.decompress(PART)
        yield data
        data = data.replace(d, b"")
        finished = decompressor.eof                     # qqqqq
        if finished == 1:
            break


decompressor = bz2.BZ2Decompressor()
data = bz2.decompress(BZIP)
d = b"".join(dstream(decompressor))

print("normstring: ", d[0:len(data)])
print("compressed: ", data)


print("normstring == compressed", d[0:len(data)] == data)
print("normstring[:10] == compressed[:10]", d[0:12] == data[0:12])
print("normstring[:10] == compressed[:10]", d[0:len(data)] == data)
print("normstring[0:10]", d[0:10])
print("compressed[0:10]", data

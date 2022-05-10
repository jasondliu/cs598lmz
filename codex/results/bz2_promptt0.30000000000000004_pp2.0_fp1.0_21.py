import bz2
# Test BZ2Decompressor

with open('data/enwik9', 'rb') as f:
    data = f.read(100)
    print(data)
    d = bz2.BZ2Decompressor()
    print(d.decompress(data))

print(d.decompress(data[:1]))
print(d.decompress(data[1:30]))
print(d.decompress(data[30:50]))
print(d.decompress(data[50:]))

print(d.decompress(data[:1]))
print(d.decompress(data[1:30]))
print(d.decompress(data[30:50]))
print(d.decompress(data[50:]))

print(d.decompress(data[:1]))
print(d.decompress(data[1:30]))
print(d.decompress(data[30:50]))
print(d.decompress(data[50:]))

print(d.decompress(

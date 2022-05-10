import bz2
bz2.decompress(data)

# bz2.decompress(data)
# data = bz2.decompress(data)
# data = bz2.decompress(data).decode()

data = bz2.decompress(data).decode()

print(data)

# data = bz2.decompress(data)
# print(data)

# data = bz2.decompress(data).decode()
# print(data)

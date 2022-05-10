import bz2
bz2.decompress(data)

# bz2.decompress(data)
# TypeError: argument 1 must be string or read-only buffer, not bytes

# bz2.decompress(str(data))
# TypeError: argument 1 must be string or read-only buffer, not str

# bz2.decompress(data.decode())
# TypeError: argument 1 must be string or read-only buffer, not str

# bz2.decompress(data.decode('utf-8'))
# TypeError: argument 1 must be string or read-only buffer, not str

# bz2.decompress(bytes(data))
# TypeError: argument 1 must be string or read-only buffer, not bytes

# bz2.decompress(bytes(data).decode())
# TypeError: argument 1 must be string or read-only buffer, not str

# bz2.decompress(bytes(data).decode('utf-8'))
# TypeError: argument 1 must be string or read-only buffer, not str


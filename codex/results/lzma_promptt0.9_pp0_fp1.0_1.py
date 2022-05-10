import lzma
# Test LZMADecompressor.
data = b'\x5d0000000000003600000000017d301d00000000000000000000000035160386037303dfc0a843c2b2'

# Reference to.
with open("dual.bin", "rb") as f:
    bkt = f.read()
    
# This is the data decoded.
xd = lzma.decompress(data)

# This is the data encoded.
x = lzma.compress(xd)

# Data sent by example.
y = xd[0:1] + bkt[len(xd):len(xd)+3] + xd[1:2] + bkt[len(xd)+3:]

# Verify that the test is valid.
if x == y:
    print("Everything is OK")
else:
    print("Damn")


# Server-side script.
s = socket.socket()
s.bind(("192.168.0.70", 80))
s.listen(1)
c, ip = s.accept()
while True:
    a = c.recv(

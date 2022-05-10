from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(b"BZ")

13 + 14 +15

#files
f = open("./binary","bw")
f.write(bytes(range(17)))
f.close()

f = open("./binary","br")
print(bytes(range(17)))

#binheks
for i in range(17):
    print("{0:>3} in hex is {0:>04x}".format(i))

x = 0x20
y = 0x0a
print(x)
print(y)
#obecnie nie działa: print(x * y)
print(x * y)

#literaly wiązane
#nic nie zadziała, bo bajty i typy w pythonie w wersji 3.8 nadal nie są zwarte
data = b'\x00\x124V\x00x\x90\xab\x00\xcd\xef\x01\x00#\x004'

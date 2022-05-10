from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(urlopen('https://github.com/MaxHalford/xam/archive/master.tar.bz2').read())

with open('xam-master.tar.bz2', 'rb') as file:
    decompressor = BZ2Decompressor()
    with open('xam-master.tar', 'wb') as output:
        for data in iter(lambda : file.read(100 * 1024), b''):
            output.write(decompressor.decompress(data))
        output.write(decompressor.flush())

BZ2Decompressor().decompress(urlopen('https://github.com/MaxHalford/xam/archive/master.tar.bz2').read())# automatically flush when EOF
BZ2Decompressor().decompress(urlopen('https://github.com/MaxHalford/xam/archive/master.tar.bz2').read())

with open('xam-master.tar.bz2', 'rb') as file, open('xam-master.tar', 'wb') as output

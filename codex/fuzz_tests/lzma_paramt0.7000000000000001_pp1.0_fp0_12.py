from lzma import LZMADecompressor
LZMADecompressor().decompress(
    open('enwik8', 'rb').read(1024 * 1024 * 1024)
).decode('utf-8')

#%%timeit
#LZMADecompressor().decompress(enwik8).decode('utf-8')

#%%timeit
#open('enwik8', 'rb').readline()

#%%timeit
#open('enwik8', 'rb').read()

#%%timeit
#open('enwik8', 'rb').read(1024 * 1024 * 1024)

#%%timeit
#open('enwik8', 'rb').read(1024 * 1024 * 1024 * 10)

#%%timeit
#open('enwik8', 'rb').read(1024 * 1024 * 1024 * 10 + 1)

#%%timeit
#open('enwik8', 'rb').read(1024 * 1024 * 1024 * 100 + 1)

#%%timeit
#open('enwik8', 'rb').read(1024 * 1024 * 1024 * 1000 + 1)

#%%timeit
#open('enwik8',

from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(bz2_data)

#%%
import bz2
bz2.decompress(bz2_data)

#%%
import bz2
uncompressed_data = b''
decompressor = bz2.BZ2Decompressor()
for chunk in iter(lambda: file.read(100 * 1024), b''):
    uncompressed_data += decompressor.decompress(chunk)

#%%
import bz2
with open('lorem.txt', 'rb') as input:
    with bz2.open('lorem.txt.bz2', 'wb') as output:
        output.writelines(input)

#%%
import bz2
with bz2.open('lorem.txt.bz2', 'rb') as input:
    with open('lorem.txt', 'wb') as output:
        for line in input:
            output.write(line)

#%%
import bz2
with open('lorem.txt', 'rb') as input:
    bz2_data

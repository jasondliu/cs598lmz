from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(bz2_data)

#%%
from urllib.request import urlopen
with urlopen('http://python.org/') as response:
    for line in response:
        line = line.decode('utf-8')  # Decoding the binary data to text.
        if 'EST' in line or 'EDT' in line:  # look for Eastern Time
            print(line)

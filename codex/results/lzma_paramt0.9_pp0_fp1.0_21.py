from lzma import LZMADecompressor
LZMADecompressor().decompress()
import io
with open('templates/C:\Users\Acer\Desktop\algo_ds\archive\comp_data/comp_data/data.csv.xz', 'rb') as f:
    x = f.read()
    decomp = LZMADecompressor()
    dec = decomp.decompress(x)
    print(dec)
 

infile = lzma.open('templates/C:\Users\Acer\Desktop\algo_ds\archive\comp_data/comp_data/data.csv.xz')
with open('outfile', 'wb') as f:
    for line in infile:
        f.write(line)

import matplotlib.pyplot as plt
print(np.histogram(data['Dos'], bins=50, range=(0,500)))
plt.hist(data['Dos'], bins=50, range=(0,500))
plt.show()
print(data['Dos'].max())
print(data['Dos'].min())
print(data

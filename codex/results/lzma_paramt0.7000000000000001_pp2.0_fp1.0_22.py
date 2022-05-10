from lzma import LZMADecompressor
LZMADecompressor().decompress(compressed_data)

# bz2
import bz2
data = bz2.compress(original_data)
len(data)
bz2.decompress(data)

# zipfile
import zipfile
filename = "test.zip"
with zipfile.ZipFile(filename, "w") as f:
    f.write("test.txt")
f.close()

zf = zipfile.ZipFile(filename, "r")
print(zf.namelist())
zf.close()

# random
import random
values = [1, 2, 3, 4, 5, 6]
# random.choice(values)
# random.sample(values, 2)
# random.shuffle(values)
# random.randint(0, 10)
# random.random()
# random.randrange(0, 101, 2)

# urllib
from urllib.request import urlopen
with urlopen("http://tycho.usno.navy.mil/cgi-bin/timer.pl") as response:

